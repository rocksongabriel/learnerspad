from django.urls import path

from ..views import DeveloperUserRetrieveView, StudentUserRetrieveView


urlpatterns = [
    path("developer/retrieve/<str:username>/", DeveloperUserRetrieveView.as_view(), name="developer-user-detail"),

    path("student/retrieve/<str:username>/", StudentUserRetrieveView.as_view(), name="student-user-detail"),
]
