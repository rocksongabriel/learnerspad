import factory
import pytest
from django.urls import reverse
from rest_framework.request import Request
from rest_framework.test import APIClient, APIRequestFactory

from ...tests.factories import DeveloperUserFactory
from ..serializers import (DeveloperUserLoginSerializer,
                           DeveloperUserRegistrationSerializer,
                           DeveloperUserRetrieveSerializer,
                           DeveloperUserUpdateSerializer)


pytestmark = pytest.mark.django_db

class TestDeveloperUserSerializers:
    
    def test_serialization__developer_user_registration_serializer(self):
        user = DeveloperUserFactory.build()
        serializer = DeveloperUserRegistrationSerializer(user)

        assert serializer.data

    
    def test_deserialization__developer_user_registration_serializer(self):
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory
        )

        serializer = DeveloperUserRegistrationSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    
    def test_serialization__developer_user_retrieve_serializer(self):
        user = DeveloperUserFactory.build()

        url = reverse("users:developer-user-detail", kwargs={"username": user.username})

        context = {
            "request": Request(APIRequestFactory().get(url))
        }

        serializer = DeveloperUserRetrieveSerializer(instance=user, context=context)

        assert serializer.data

    
    def test_deserialization__developer_user_retrieve_serializer(self):
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory,
        )

        serializer = DeveloperUserRetrieveSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    
    def test_serialization__developer_user_update_serializer(self):
        user = DeveloperUserFactory.build()

        serializer = DeveloperUserUpdateSerializer(user)

        assert serializer.data

    
    def test_deserialization__developer_user_update_serializer(self):
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory
        )

        serializer = DeveloperUserUpdateSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    
    def test_serialization__developer_user_login_serializer(self):
        user = DeveloperUserFactory.build()
        serializer = DeveloperUserLoginSerializer(user)

        assert serializer.data

    
    def test_deserialization__developer_user_login_serializer(self):
        json_data = factory.build(
            dict,
            FACTORY_CLASS=DeveloperUserFactory
        )

        serializer = DeveloperUserLoginSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}
