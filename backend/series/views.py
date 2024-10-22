from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status

api_key = '51994fc2e7969ea0e9a79d6a0f95fa63'
language = 'tr-TR'

class GetAllSeriesView(APIView):
      def get(self, request):
            url = f'https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language={language}'

            response = requests.get(url)
            if response.status_code == 200:
                  data = response.json()
                  return Response(data)
            return Response({"message": "error.!"}, status=response.status_code)
      
      
class SearchSeriesByName(APIView):
      def post(self, request):
            query = request.data.get('query')  
            
            if not query:
                  return Response({'message':'Query field is required'})
            
            url = f'https://api.themoviedb.org/3/search/tv?include_adult=true&api_key={api_key}&language={language}&query={query}'
            response = requests.get(url)
            
            if response.status_code == 200:
                  data = response.json()
                  return Response(data)
            return Response({'message':'error.!'})
      
      
class GetSeriesByActor(APIView):
      def post(self,request):
            actor_name = request.data.get('actor')
            
            if not actor_name:
                  return Response({'message':'actor field is required'},status=status.HTTP_400_BAD_REQUEST)
            
            actor_url = f'https://api.themoviedb.org/3/search/person?api_key={api_key}&language={language}&query={actor_name}'
            actor_response = requests.get(actor_url)
            if actor_response.status_code == 200:
                  actor_data = actor_response.json().get('results',[])
                  if not actor_data:
                        return Response({'message':'Actor not found'},status=status.HTTP_404_NOT_FOUND)
                  actor_id = actor_data[0]['id']
                  
                  series_url = f'https://api.themoviedb.org/3/person/{actor_id}/tv_credits?api_key={api_key}&language={language}'
                  series_response = requests.get(series_url)
                  if series_response.status_code == 200:
                        series_response = series_response.json().get('cast',[])
                        selected_series = [
                              {'title': series['name'], 'original_title': series['original_name']}
                              for series in series_response
                        ]
                        return Response(selected_series,status=status.HTTP_200_OK)
            return Response({'message':'Error.'})
      
      
class GetTopSeriesByYear(APIView):
      def post(self,request):
            year = request.data.get('year')
            sort_by = "vote_average.desc"
            
            if not year:
                  return Response({'message':'year field is required'},status=status.HTTP_400_BAD_REQUEST)
            
            if not isinstance(year,int):
                  return Response({'message':'Year field must be an integer'},status=status.HTTP_400_BAD_REQUEST)
            
            if year < 1000 or year > 9999:
                  return Response({'message':'Year must be a 4-digit number'},status=status.HTTP_400_BAD_REQUEST)
            
            series_url = f'https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language={language}&first_air_date_year={year}&sort_by={sort_by},'
            series_response = requests.get(series_url)
            if series_response.status_code == 200:
                  series_response = series_response.json().get('results',[])
                  selected_series = [
                        {'title': series['name'], 'original_title': series['original_name']}
                        for series in series_response
                  ]
                  return Response(selected_series,status=status.HTTP_200_OK)
            return Response({'message':'Error'})