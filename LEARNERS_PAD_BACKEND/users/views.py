from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from .api.serializers import DeveloperUserLoginSerializer, DeveloperUserRegistrationSerializer, DeveloperUserRetrieveSerializer, StudentUserRegistrationSerializer, StudentUserRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


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


# class DeveloperUserLoginView(APIView):
#     """APIView to login a developer user"""

#     # take the user username and password
#     # send the data to the obtain_token endpoint
#     # get the access and refresh tokens
#     # make an api call to the retrieve endpoint
#     # get the url field of the user
#     # form the response of the operation

#     def post(self, request):
#         serializer = DeveloperUserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data["username"]
#             password = serializer.validated_data["password"]




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