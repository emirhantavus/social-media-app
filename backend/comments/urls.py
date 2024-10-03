from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from comments.views import CommentCreateView , CommentRetrieveUpdateAndDestroyView

urlpatterns = [
      path('posts/<int:post_id>/comments/',CommentCreateView.as_view(),name='comment'),
      path('posts/<int:post_id>/comments/<int:comment_id>/',CommentRetrieveUpdateAndDestroyView.as_view(),name='update-comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
