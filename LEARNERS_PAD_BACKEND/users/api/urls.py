from django.urls import path

from ..views import DeveloperUserRetrieveView


urlpatterns = [
    path("developer/retrieve/<str:username>/", DeveloperUserRetrieveView.as_view(), name="developer-user-detail"),
]
