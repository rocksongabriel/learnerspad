from rest_framework import serializers
from ..models import DeveloperUser, DeveloperUserProfile, StudentUser, StudentUserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token obtain pair serializer"""

    @classmethod
    def get_token(cls, user):
        token =  super().get_token(user)

        # add custom claims
        token['uuid'] = str(user.uuid)

        return token


class DeveloperUserRegistrationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DeveloperUser
        fields = ["username", "email", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }


class DeveloperUserRetrieveSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="users:developer-user-detail",
        source="uuid",
        lookup_field="uuid",
        lookup_url_kwarg="uuid"
    )

    class Meta:
        model = DeveloperUser
        fields = ["id", "url", "username", "email", "first_name", "last_name", "type"]


class DeveloperUserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeveloperUser
        fields = ["username", "email", "first_name", "last_name"]


class StudentUserRegistrationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StudentUser
        fields = ["username", "email", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

class StudentUserRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="users:student-user-detail",
        lookup_field="uuid",
        source="uuid",
        lookup_url_kwarg="uuid"
    )

    class Meta:
        model = StudentUser
        fields = ["id", "url", "username", "email", "first_name", "last_name", "type"]


class StudentUserUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StudentUser
        fields = ["username", "email", "first_name", "last_name"]


class DeveloperUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for a Developer user typer profile"""

    class Meta:
        model = DeveloperUserProfile
        fields = ["bio"]


class StudentUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for a student user type profile"""

    class Meta:
        model = StudentUserProfile
        fields = ["bio"]