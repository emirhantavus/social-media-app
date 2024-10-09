from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieSerializer
import requests

class MovieListCreateView(generics.ListCreateAPIView):
      queryset = Movie.objects.all()
      serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Movie.objects.all()
      serializer_class = MovieSerializer

class GetMoviesView(APIView):
      def get(self, request):
            api_key = '51994fc2e7969ea0e9a79d6a0f95fa63'
            language = 'tr-TR'
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


#https://developer.themoviedb.org/reference/search-movie