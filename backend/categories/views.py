from rest_framework import generics , permissions
from .models import Category, Genre
from .serializers import CategorySerializer, GenreSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
      queryset = Category.objects.all()
      serializer_class = CategorySerializer
      
      
class GenreListCreateView(generics.ListCreateAPIView):
      queryset = Genre.objects.all()
      serializer_class = GenreSerializer