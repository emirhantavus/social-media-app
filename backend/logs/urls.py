from django.urls import path
from logs.views import ListIPLogsView , ListActionLogsView , GenerateAPIKey , RetrieveAPIKey , ListAllAPIKey , DeleteAPIkey

urlpatterns = [
    path('user-logs/',ListIPLogsView.as_view(),name='user-logs'),
    path('movie-logs/',ListActionLogsView.as_view(),name='movies-logs'),
    path('generate-api-key/',GenerateAPIKey.as_view(),name='generate_api_key'),
    path('retrieve-api-key/',RetrieveAPIKey.as_view(),name='retrieve_api_key'),
    path('list-api-key/',ListAllAPIKey.as_view(),name='list_api_key'), 
    path('delete-api-key/',DeleteAPIkey.as_view(),name='delete_api_key'),
]
