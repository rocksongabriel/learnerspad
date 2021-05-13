import factory
import pytest
from ...tests.factories import DeveloperUserFactory
from ..serializers import DeveloperUserLoginSerializer, DeveloperUserRegistrationSerializer, DeveloperUserRetrieveSerializer, DeveloperUserUpdateSerializer
import factory
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.request import Request
from django.urls import reverse


@pytest.mark.django_db
def test_serialization__developer_user_registration_serializer():
    user = DeveloperUserFactory.build()
    serializer = DeveloperUserRegistrationSerializer(user)

    assert serializer.data

@pytest.mark.django_db
def test_deserialization__developer_user_registration_serializer():
    json_data = factory.build(
        dict,
        FACTORY_CLASS = DeveloperUserFactory
    )

    serializer = DeveloperUserRegistrationSerializer(data=json_data)

    assert serializer.is_valid()
    assert serializer.errors == {}

@pytest.mark.django_db
def test_serialization__developer_user_retrieve_serializer():
    user = DeveloperUserFactory.build()

    url = reverse("users:developer-user-detail", kwargs={"username": user.username})

    context = {
        "request": Request(APIRequestFactory().get(url))
    }

    serializer = DeveloperUserRetrieveSerializer(instance=user, context=context)

    assert serializer.data

@pytest.mark.django_db
def test_deserialization__developer_user_retrieve_serializer():
    json_data = factory.build(
        dict,
        FACTORY_CLASS = DeveloperUserFactory,
    )

    serializer = DeveloperUserRetrieveSerializer(data=json_data)

    assert serializer.is_valid()
    assert serializer.errors == {}

@pytest.mark.django_db
def test_serialization__developer_user_update_serializer():
    user = DeveloperUserFactory.build()

    serializer = DeveloperUserUpdateSerializer(user)

    assert serializer.data

@pytest.mark.django_db
def test_deserialization__developer_user_update_serializer():
    json_data = factory.build(
        dict,
        FACTORY_CLASS = DeveloperUserFactory
    )

    serializer = DeveloperUserUpdateSerializer(data=json_data)

    assert serializer.is_valid()
    assert serializer.errors == {}

@pytest.mark.django_db
def test_serialization__developer_user_login_serializer():
    user = DeveloperUserFactory.build()
    serializer = DeveloperUserLoginSerializer(user)

    assert serializer.data

@pytest.mark.django_db
def test_deserialization__developer_user_login_serializer():
    json_data = factory.build(
        dict,
        FACTORY_CLASS=DeveloperUserFactory
    )

    serializer = DeveloperUserLoginSerializer(data=json_data)

    assert serializer.is_valid()
    assert serializer.errors == {}