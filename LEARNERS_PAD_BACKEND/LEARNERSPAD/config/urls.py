from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls from third party applications
    path('api-auth/', include('rest_framework.urls')),

    # App urls
    path("api/", include("users.urls", namespace="users")),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)