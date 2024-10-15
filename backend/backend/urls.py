from django.contrib import admin
from django.urls import path ,include
from drf_spectacular.views import SpectacularAPIView , SpectacularRedocView , SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/',include('users.urls')),
    path('api/v1/posts/',include('posts.urls')),
    path('api/v1/comments/',include('comments.urls')),
    path('api/v1/movies/',include('movies.urls')),
    path('api/v1/categories/',include('categories.urls')),
    path('api/v1/logs/',include('logs.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)