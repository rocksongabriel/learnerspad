from rest_framework import serializers
from ..models import DeveloperUser, DeveloperUserProfile, StudentUser, StudentUserProfile


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
        source="username",
        lookup_field="username",
        lookup_url_kwarg="username"
    )

    class Meta:
        model = DeveloperUser
        fields = ["id", "url", "username", "email", "first_name", "last_name", "type"]


class DeveloperUserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeveloperUser
        fields = ["username", "email", "first_name", "last_name"]


class DeveloperUserLoginSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DeveloperUser
        fields = ["username", "password"]


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
        lookup_field="username",
        source="username",
        lookup_url_kwarg="userame"
    )

    class Meta:
        model = StudentUser
        fields = ["id", "url", "username", "email", "first_name", "last_name", "type"]


class StudentUserUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StudentUser
        fields = ["username", "email", "first_name", "last_name"]


class StudentUserLoginSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StudentUser
        fields = ["username", "password"]


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