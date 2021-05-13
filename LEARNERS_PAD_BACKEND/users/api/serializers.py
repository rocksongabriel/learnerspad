from rest_framework import serializers
from ..models import DeveloperUser


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
