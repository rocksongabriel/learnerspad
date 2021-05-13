import factory
import pytest
from ...tests.factories import DeveloperUserFactory
from ..serializers import DeveloperUserRegistrationSerializer
import factory


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