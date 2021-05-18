from django.urls import path

from ..views import (DeveloperUserRegisterView, DeveloperUserRetrieveView,
                     StudentUserRegisterView, StudentUserRetrieveView,
                     UserLoginAPIView)

urlpatterns = [
    path("developer/retrieve/<str:uuid>/", DeveloperUserRetrieveView.as_view(), name="developer-user-detail"),
    path("developer/create/", DeveloperUserRegisterView.as_view(), name="developer-user-create"),

    path("student/retrieve/<str:uuid>/", StudentUserRetrieveView.as_view(), name="student-user-detail"),
    path("student/create/", StudentUserRegisterView.as_view(), name="student-user-create"),

    path("login/", UserLoginAPIView.as_view(), name="login"),
]
