from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView , GetMoviesView

urlpatterns = [
    path('', GetMoviesView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
]
