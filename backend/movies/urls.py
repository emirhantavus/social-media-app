from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView , GetMoviesView , GetMovieByTitleView

urlpatterns = [
    path('', GetMoviesView.as_view(), name='movie-list'),
    path('get-movie-by-title/', GetMovieByTitleView.as_view(), name='movie-detail'),
]
