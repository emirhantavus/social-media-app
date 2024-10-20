from django.urls import path
from .views import (
        MovieListCreateView, MovieRetrieveUpdateDestroyView ,
        GetMoviesView , GetMovieByTitleView , GetMovieByActorView,
        GetMoviesByGenreView)

urlpatterns = [
    path('', GetMoviesView.as_view(), name='movie-list'),
    path('get-movie-by-title/', GetMovieByTitleView.as_view(), name='movie-detail'),
    path('get-movie-by-actor/', GetMovieByActorView.as_view(), name='movie-actor'),
    path('get-movie-by-genre/', GetMoviesByGenreView.as_view(), name='movie-genre'),
]
