from django.urls import path
from .views import (
        MovieListCreateView, MovieRetrieveUpdateDestroyView ,
        GetMoviesView , GetMovieByTitleView , GetMovieByActorView,
        GetMoviesByGenreView, GetMoviesByYearView, GetTopMoviesView)

urlpatterns = [
    path('', GetMoviesView.as_view(), name='movie-list'),
    path('get-movie-by-title/', GetMovieByTitleView.as_view(), name='movie-detail'),
    path('get-movie-by-actor/', GetMovieByActorView.as_view(), name='movie-actor'),
    path('get-movie-by-genre/', GetMoviesByGenreView.as_view(), name='movie-genre'),
    path('get-movie-by-year/', GetMoviesByYearView.as_view(), name='movie-year'),
    path('get-movie-top/', GetTopMoviesView.as_view(), name='movie-top'),
]
