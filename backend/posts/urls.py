from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import PostListView , PostRetriveAndUpdateView

urlpatterns = [
      path('',PostListView.as_view(),name='post-list'),
      path('<int:pk>/',PostRetriveAndUpdateView.as_view(),name='post-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
