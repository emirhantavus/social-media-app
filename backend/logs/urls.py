from django.urls import path
from logs.views import ListIPLogsView

urlpatterns = [
    path('user-logs/',ListIPLogsView.as_view(),name='user-logs'),
]
