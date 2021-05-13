import factory
import pytest
from django.urls import reverse
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from ...tests.factories import DeveloperUserFactory, StudentUserFactory
from ..serializers import (DeveloperUserLoginSerializer,
                           DeveloperUserRegistrationSerializer,
                           DeveloperUserRetrieveSerializer,
                           DeveloperUserUpdateSerializer, StudentUserLoginSerializer, StudentUserRegistrationSerializer, StudentUserRetrieveSerializer, StudentUserUpdateSerializer)


pytestmark = pytest.mark.django_db

class TestDeveloperUserSerializers:
    """Tests for the Serializers associated with the Developer User type"""

    def test_serialization__developer_user_registration_serializer(self):
        """test for serializer of the developer user registration serializer"""
        user = DeveloperUserFactory.build()
        serializer = DeveloperUserRegistrationSerializer(user)

        assert serializer.data

    
    def test_deserialization__developer_user_registration_serializer(self):
        """test for deserialization of the developer user registration serializer"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory
        )

        serializer = DeveloperUserRegistrationSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    
    def test_serialization__developer_user_retrieve_serializer(self):
        """test for serialization of the developer user retrieve serializer"""
        user = DeveloperUserFactory.build()

        url = reverse("users:developer-user-detail", kwargs={"username": user.username})

        context = {
            "request": Request(APIRequestFactory().get(url))
        }

        serializer = DeveloperUserRetrieveSerializer(instance=user, context=context)

        assert serializer.data

    
    def test_deserialization__developer_user_retrieve_serializer(self):
        """test for deserialization of the developer user retrieve serialization"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory,
        )

        serializer = DeveloperUserRetrieveSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    
    def test_serialization__developer_user_update_serializer(self):
        """test for serialization of the developer user update serializer"""
        user = DeveloperUserFactory.build()

        serializer = DeveloperUserUpdateSerializer(user)

        assert serializer.data

    
    def test_deserialization__developer_user_update_serializer(self):
        """test for the deserialization of the developer user update serializer"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory
        )

        serializer = DeveloperUserUpdateSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    
    def test_serialization__developer_user_login_serializer(self):
        """test for the serialization of the developer user login serializer"""
        user = DeveloperUserFactory.build()
        serializer = DeveloperUserLoginSerializer(user)

        assert serializer.data

    
    def test_deserialization__developer_user_login_serializer(self):
        """test for the deserialization of the developer user login serializer"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS=DeveloperUserFactory
        )

        serializer = DeveloperUserLoginSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}


class TestStudentUserSerializers:
    """Tests for the student user type  serializers"""

    def test_serialization__student_user_registration_serializer(self):
        """test for the serialization of data of the student user registration serializer"""
        user = StudentUserFactory.build()

        serializer = StudentUserRegistrationSerializer(user)

        assert serializer.data

    def test_deserialization__student_user_registration_serializer(self):
        """test for the deserialization of data of the student user registration serializer"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS = StudentUserFactory
        )

        serializer = StudentUserRegistrationSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    def test_serialization__student_user_retrieve_serializer(self):
        """test for the serialization of data of the student user retrieve serializer"""
        user = StudentUserFactory.build()

        url = reverse("users:student-user-detail", kwargs={"username": user.username})

        context = {
            "request": Request(APIRequestFactory().get(url))
        }

        serializer = StudentUserRetrieveSerializer(instance=user, context=context)

        assert serializer.data

    def test_deserialization__student_user_retrieve_serializer(serlf):
        """test for the deserialization of data of the student user retrive serializer"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS = StudentUserFactory
        )

        serializer = StudentUserRetrieveSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}
    

    def test_serialization__student_user_update_serializer(self):
        """test for the serialization of data of the student user update serializer"""
        user = StudentUserFactory.build()

        serializer = StudentUserUpdateSerializer(user)

        assert serializer.data

    def test_deserialization__student_user_update_serializer(self):
        """test for the deserialization of data of the student user update serializer"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS=StudentUserFactory
        )

        serializer = StudentUserUpdateSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}

    def test_serializer__student_user_login_serializer(self):
        """test for the serializer of data of the student user login serializer"""
        user = StudentUserFactory.build()
        
        serializer = StudentUserLoginSerializer(user)

        assert serializer.data

    def test_deserialization__student_user_login_serializer(self):
        """test for the deserialization of data of the student user login serializer"""
        json_data = factory.build(
            dict,
            FACTORY_CLASS=StudentUserFactory
        )

        serializer = StudentUserLoginSerializer(data=json_data)

        assert serializer.is_valid()
        assert serializer.errors == {}