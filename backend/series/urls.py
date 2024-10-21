from django.urls import path
from series.views import GetAllSeriesView , SearchSeriesByName , GetSeriesByActor

urlpatterns = [
    path('', GetAllSeriesView.as_view(), name='series-list'),
    path('search/', SearchSeriesByName.as_view(), name='search-series'),
    path('get-series-by-actor/', GetSeriesByActor.as_view(), name='series-actor'),
]
