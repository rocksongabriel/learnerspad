import pytest
from .factories import DeveloperUserFactory
from .utils import get_user_data


# APIClient fixture
@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


# Developer User object fixture
@pytest.fixture
def developer_user():
    generated_user = DeveloperUserFactory.build()
    user_data = get_user_data(generated_user)
    return user_data