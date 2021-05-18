import json
from django.contrib.auth import get_user, get_user_model
import jwt
import requests
from django.urls import reverse
from requests.api import options
from rest_framework import response, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.serializers import CustomTokenObtainPairSerializer

from .api.serializers import (DeveloperUserRegistrationSerializer,
                              DeveloperUserRetrieveSerializer,
                              StudentUserRegistrationSerializer,
                              StudentUserRetrieveSerializer)

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom token obtain pair view"""
    serializer_class = CustomTokenObtainPairSerializer


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


class BaseUserLoginView(APIView):

    user_type = ""

    def post(self, request):
        req_data = request.data
        url = "http://localhost:8000" + reverse("users:token_obtain_pair") # todo - modify how this is constructed so that it works in production
        res = requests.post(
            url,
            data={
                "username": req_data["username"],
                "password": req_data["password"]
            }
        )
        user_retrieve_url = reverse(f"users:{self.user_type}-user-detail", kwargs={"username":req_data["username"]})
        if res.status_code == 200:
            data = {}
            data["user_retrieve_url"] = user_retrieve_url
            data["token"] = json.loads(res.content)
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = json.loads(res.content)
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

class DeveloperUserRegisterView(BaseUserRegisterView):
    """APIView to create a developer user instance"""

    serializer = DeveloperUserRegistrationSerializer


class DeveloperUserLoginView(BaseUserLoginView):
    """API view to log in a developer user"""

    user_type = "developer"


class DeveloperUserRetrieveView(RetrieveAPIView):
    """APIView to retrieve a particular developer user instance"""

    serializer_class = DeveloperUserRetrieveSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"


class StudentUserRegisterView(BaseUserRegisterView):
    """APIView to create a student user instance"""

    serializer = StudentUserRegistrationSerializer


class StudentUserLoginView(BaseUserLoginView):
    """APIView to login a student user"""

    user_type = "student"


class StudentUserRetrieveView(RetrieveAPIView):
    """APIView to retrieve a particular student user instance"""

    serializer_class = StudentUserRetrieveSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"



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
            user = User.objects.get(uuid=decoded_token["uuid"])
            user_retrieve_url = reverse(f"users:{user.type.lower()}-user-detail", kwargs={"username":request_data["username"]})

            data["user_retrieve_url"] = user_retrieve_url

            return Response(data, status=status.HTTP_200_OK)
        else:
            data = json.loads(res.content)
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
