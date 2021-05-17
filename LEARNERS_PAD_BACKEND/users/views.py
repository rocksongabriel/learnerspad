from rest_framework import response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from .api.serializers import DeveloperUserLoginSerializer, DeveloperUserRegistrationSerializer, DeveloperUserRetrieveSerializer, StudentUserRegistrationSerializer, StudentUserRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import requests
from django.urls import reverse
import json


class BaseUserRegisterView(APIView):
    serializer = ""

    def post(self, request):
        serializer = self.serializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data["password"])
            user.save()
            data["message"] = "User {} has been created successfully".format(user.username)
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class DeveloperUserRegisterView(BaseUserRegisterView):
    """APIView to create a developer user instance"""

    serializer = DeveloperUserRegistrationSerializer


class DeveloperUserLoginView(APIView):
    """APIView to login a developer user"""

    def post(self, request):
        data = {}

        serializer = DeveloperUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            # make api call to token endpoint for token
            url = reverse("token_obtain_pair")
            res = requests.post(url, data={
                "username": username,
                "password": password,
            })
            if res.status_code == 200:
                data["message"] = "User logged in successfully"
            data["token"] = json.loads(res.content)
            data["retrieve_user_url"] = reverse("users:developer-user-detail", kwargs={"username": username})

            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class DeveloperUserRetrieveView(RetrieveAPIView):
    """APIView to retrieve a particular developer user instance"""

    serializer_class = DeveloperUserRetrieveSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"



class StudentUserRegisterView(BaseUserRegisterView):
    """APIView to create a student user instance"""

    serializer = StudentUserRegistrationSerializer


class StudentUserRetrieveView(RetrieveAPIView):
    """APIView to retrieve a particular student user instance"""

    serializer_class = StudentUserRetrieveSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"