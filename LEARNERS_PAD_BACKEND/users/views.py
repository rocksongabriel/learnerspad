import json
from collections import ChainMap
from django.db.models import query

import jwt
import requests
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.serializers import CustomTokenObtainPairSerializer

from .api.serializers import (DeveloperUserProfileSerializer,
                              DeveloperUserRegistrationSerializer,
                              DeveloperUserRetrieveSerializer,
                              StudentUserProfileSerializer,
                              StudentUserRegistrationSerializer,
                              StudentUserRetrieveSerializer)
from .models import (DeveloperUser, DeveloperUserProfile, StudentUser,
                     StudentUserProfile)

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom token obtain pair view"""
    serializer_class = CustomTokenObtainPairSerializer


class BaseUserRegisterView(APIView):
    serializer = None

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


class BaseUserRetrieveView(RetrieveAPIView):
    """Base APIView to retrieve a particular user instance"""
    profile_serializer = None
    profile_model = None
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() #  get current instance
        user_profile = self.profile_model.objects.get(user=instance) # get the profile associated with the user instance
        profile_serializer = self.profile_serializer(user_profile) # serialize the profile data
        serializer = self.get_serializer(instance)
        data = dict(ChainMap(serializer.data, profile_serializer.data)) # Add the user data and profile data

        return Response(data, status=status.HTTP_200_OK)

class DeveloperUserRegisterView(BaseUserRegisterView):
    """APIView to create a developer user instance"""

    serializer = DeveloperUserRegistrationSerializer


class DeveloperUserRetrieveView(BaseUserRetrieveView):
    """APIView to retrieve a particular developer user instance"""
    profile_model = DeveloperUserProfile
    profile_serializer = DeveloperUserProfileSerializer
    queryset = DeveloperUser.objects.all()
    serializer_class = DeveloperUserRetrieveSerializer

class StudentUserRegisterView(BaseUserRegisterView):
    """APIView to create a student user instance"""

    serializer = StudentUserRegistrationSerializer


class StudentUserRetrieveView(BaseUserRetrieveView):
    """APIView to retrieve a particular student user instance"""
    profile_model = StudentUserProfile
    profile_serializer = StudentUserProfileSerializer
    queryset = StudentUser.objects.all()
    serializer_class = StudentUserRetrieveSerializer


class UserLoginAPIView(APIView):
    """ API view to log any type of user in """

    def post(self, request):
        request_data = request.data
        data = {}

        url = "http://localhost:8000" + reverse("users:token_obtain_pair") # todo - modify how this is constructed so that it works in production

        res = requests.post(
            url,
            data = {
                "username": request_data["username"],
                "password": request_data["password"],
            }
        )

        if res.status_code == 200:
            data["token"] = json.loads(res.content)

            decoded_token = jwt.decode(data["token"]["access"], options={"verify_signature": False})
            uuid = decoded_token["uuid"]
            user = User.objects.get(uuid=uuid)
            user_retrieve_url = reverse(f"users:{user.type.lower()}-user-detail", kwargs={"uuid": uuid})

            data["user_retrieve_url"] = user_retrieve_url
            data["message"] = "Login successful"

            return Response(data, status=status.HTTP_200_OK)
        else:
            data = json.loads(res.content)
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
