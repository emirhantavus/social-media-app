from django.urls import path
from series.views import GetAllSeriesView , SearchSeriesByName

urlpatterns = [
    path('', GetAllSeriesView.as_view(), name='series-list'),
    path('search/', SearchSeriesByName.as_view(), name='search-series'),
]
