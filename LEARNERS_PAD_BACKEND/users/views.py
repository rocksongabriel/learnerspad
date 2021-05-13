from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .api.serializers import DeveloperUserRetrieveSerializer


class DeveloperUserRetrieveView(RetrieveAPIView):
    serializer_class = DeveloperUserRetrieveSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"