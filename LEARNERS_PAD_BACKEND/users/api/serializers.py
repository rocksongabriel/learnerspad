from rest_framework import serializers
from ..models import DeveloperUser, StudentUser


class DeveloperUserRegistrationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DeveloperUser
        fields = ["username", "email", "password"]


class DeveloperUserRetrieveSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="users:developer-user-detail",
        source="username",
        lookup_field="username",
        lookup_url_kwarg="username"
    )

    class Meta:
        model = DeveloperUser
        fields = ["id", "url", "username", "email", "first_name", "last_name"]


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


class StudentUserRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="users:student-user-detail",
        lookup_field="username",
        source="username",
        lookup_url_kwarg="userame"
    )

    class Meta:
        model = StudentUser
        fields = ["id", "url", "username", "email", "first_name", "last_name"]


class StudentUserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = StudentUser
        fields = ["username", "email", "first_name", "last_name"]