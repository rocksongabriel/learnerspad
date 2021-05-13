from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls from third party applications
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # App urls
    path("api", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)