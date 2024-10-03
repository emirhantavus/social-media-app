from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import PostListView , PostRetrieveUpdateAndDestroyView

urlpatterns = [
      path('',PostListView.as_view(),name='post-list'),
      path('<int:pk>/',PostRetrieveUpdateAndDestroyView.as_view(),name='post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
