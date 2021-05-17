from django.urls import path

from ..views import (DeveloperUserRegisterView, DeveloperUserRetrieveView, DeveloperUserLoginView,
                     StudentUserRetrieveView, StudentUserRegisterView)

urlpatterns = [
    path("developer/retrieve/<str:username>/", DeveloperUserRetrieveView.as_view(), name="developer-user-detail"),
    path("developer/create/", DeveloperUserRegisterView.as_view(), name="developer-user-create"),
    path("developer/login/", DeveloperUserLoginView.as_view(), name="developer-user-login"),

    path("student/retrieve/<str:username>/", StudentUserRetrieveView.as_view(), name="student-user-detail"),
    path("student/create/", StudentUserRegisterView.as_view(), name="student-user-create"),
]
