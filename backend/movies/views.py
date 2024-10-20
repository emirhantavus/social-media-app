from rest_framework import generics, permissions , status
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer
import requests
from rest_framework.pagination import PageNumberPagination

api_key = '51994fc2e7969ea0e9a79d6a0f95fa63'
language = 'tr-TR'

class MoviePagination(PageNumberPagination):
      page_size = 20

class MovieListCreateView(generics.ListCreateAPIView):
      queryset = Movie.objects.all().order_by('id')
      serializer_class = MovieSerializer
      pagination_class = MoviePagination

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Movie.objects.all()
      serializer_class = MovieSerializer

class GetMoviesView(APIView):
      def get(self, request):
            url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language={language}'

            response = requests.get(url)
            data = response.json()

            return Response(data)
  
class GetMovieByTitleView(APIView):
      def post(self, request):
            title = request.data.get('title', '')
            movies = Movie.objects.filter(title__icontains=title)
            if movies.exists():
                  movie_list = [
                  {
                        'title': movie.title,
                        'overview': movie.overview,
                        'release_date': movie.release_date,
                        'poster_path': movie.poster_path,
                        'language': movie.language,
                  }
                  for movie in movies
                ] 
                  return Response({"movie_count":movies.count(),"movies":movie_list})
            return Response({"message": "Film bulunamadı"}, status=404)

class GetMovieByActorView(APIView):
      def post(self, request):
            actor = request.data.get('actor')
            
            if not actor:
                  return Response({'message':'Actor field is required'},status=status.HTTP_400_BAD_REQUEST)
            
            actor_url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&language={language}&query={actor}'
            actor_response = requests.get(actor_url)
            if actor_response.status_code == 200:
                  actor_data = actor_response.json().get('results', [])
                  if actor_data:
                        actor_id = actor_data[0]['id']
                        movies_url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={language}&with_cast={actor_id}'
                        movie_response = requests.get(movies_url)
                        if movie_response.status_code == 200:
                              movie_data = movie_response.json().get('results',[])
                              filtered_movies = [
                                    {'title': movie['title'] , 'original_title':movie['original_title']}
                                    for movie in movie_data
                              ]
                              return Response(filtered_movies)
            return Response({'message': 'Error fetching actor movies'}, status=status.HTTP_400_BAD_REQUEST)
      

class GetMoviesByGenreView(APIView):
      def post(self,request):
            genre = request.data.get('genre')
            
            if not genre:
                  return Response({'message':'Genre field is required.'})
            
            genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language={language}"
            genre_response = requests.get(genre_url)
            
            if genre_response.status_code == 200:
                  genres = genre_response.json().get('genres',[])
                  genre_id = next((g['id'] for g in genres if g['name'].lower() == genre.lower()),None)
                  if genre_id:
                        movies_url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={language}&with_genres={genre_id}"
                        movie_response = requests.get(movies_url)
                        if movie_response.status_code == 200:
                              movie_data = movie_response.json().get('results',[])
                              filtered_movies = [
                                    {'title':movie['title'],'original_title':movie['original_title']}
                                    for movie in movie_data
                              ]
                              return Response(filtered_movies)
            return Response({'message':'Error.'})
      
#https://developer.themoviedb.org/reference/search-movie