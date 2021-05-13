from rest_framework import serializers
from ..models import DeveloperUser


class DeveloperUserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = DeveloperUser
        fields = ["username", "email", "password"]
