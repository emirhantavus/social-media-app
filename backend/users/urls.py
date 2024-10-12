from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import (
      RegisterView,
      LoginView,
      UserProfileView,
      UserList,
      FollowView,
      LogOutView,
      DeleteUserView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
      path('register/', RegisterView.as_view(), name='register'),
      path('login/', LoginView.as_view(), name='login'),
      path('logout/',LogOutView.as_view(),name='logout'),
      path('delete/',DeleteUserView.as_view(),name='delete-account'),
      path('profile/<int:pk>',UserProfileView.as_view(),name='user_profile'),
      path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      path('follow/<int:user_id>/',FollowView.as_view(),name='follow_user'),
      path('',UserList.as_view(),name='user_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
