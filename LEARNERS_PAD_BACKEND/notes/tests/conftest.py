import pytest
from users.tests.factories import DeveloperUserFactory, StudentUserFactory
from users.tests.utils import get_user_data

# Student User object fixture
@pytest.fixture
def student_user():
    generated_user = StudentUserFactory.build()
    user_data = get_user_data(generated_user)
    return user_data