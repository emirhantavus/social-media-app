from django.urls import path
from logs.views import ListIPLogsView , ListActionLogsView

urlpatterns = [
    path('user-logs/',ListIPLogsView.as_view(),name='user-logs'),
    path('movie-logs/',ListActionLogsView.as_view(),name='movies-logs')
]
