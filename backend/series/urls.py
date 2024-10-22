from django.urls import path
from series.views import (GetAllSeriesView , SearchSeriesByName , 
                          GetSeriesByActor , GetTopSeriesByYear , GetTopSeries,
                          GetSeriesByGenreView)

urlpatterns = [
    path('', GetAllSeriesView.as_view(), name='series-list'),
    path('search/', SearchSeriesByName.as_view(), name='search-series'),
    path('get-series-by-actor/', GetSeriesByActor.as_view(), name='series-actor'),
    path('get-top-series-by-year/', GetTopSeriesByYear.as_view(), name='series-year'),
    path('get-top-series/', GetTopSeries.as_view(), name='series-top'),
    path('get-series-by-genre/', GetSeriesByGenreView.as_view(), name='series-genre'),
]
