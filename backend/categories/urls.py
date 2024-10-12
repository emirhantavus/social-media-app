from django.urls import path, include
from .views import CategoryListCreateView, GenreListCreateView


urlpatterns = [
      path('', CategoryListCreateView.as_view(),name='category-list'),
      path('genres/', GenreListCreateView.as_view(),name='genre-list'),
]
