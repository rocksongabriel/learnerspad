from re import S
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from .api.serializers import DeveloperUserRegistrationSerializer, DeveloperUserRetrieveSerializer, StudentUserRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class DeveloperUserRegisterView(APIView):
    """APIView to create a developer user instance"""

    def post(self, request):
        serializer = DeveloperUserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["message"] = "User {} has been created successfully".format(user.username)
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class DeveloperUserRetrieveView(RetrieveAPIView):
    """APIView to retrieve a particular developer user instance"""

    permission_classes = [IsAuthenticated]
    serializer_class = DeveloperUserRetrieveSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"


class StudentUserRetrieveView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentUserRetrieveSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"