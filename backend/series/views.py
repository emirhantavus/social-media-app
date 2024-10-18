from rest_framework.views import APIView
from rest_framework.response import Response
import requests

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