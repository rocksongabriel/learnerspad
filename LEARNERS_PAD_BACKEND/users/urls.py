from django.urls import path, include


app_name="users"
urlpatterns = [
    path("users/account/", include("users.api.urls")),
]
