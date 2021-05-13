import pytest
from .factories import DeveloperUserFactory, StudentUserFactory
from ..models import DeveloperUser, StudentUser
from .utils import get_user_data


pytestmark = pytest.mark.django_db

class TestUserObjectCreation:

    def test_single_developer_user_object_creation(self):
        generated_user = DeveloperUserFactory.build()
        user_data = get_user_data(generated_user)
        DeveloperUser.objects.create(**user_data)

        assert DeveloperUser.objects.count() == 1

    def test_created_developer_user_has_specified_data(self):
        generated_user = DeveloperUserFactory.build()
        user_data = get_user_data(generated_user)
        user = DeveloperUser.objects.create(**user_data)

        assert user.username == generated_user.username

    def test_type_of_created_developer_user(self):
        generated_user = DeveloperUserFactory.build()
        user_data = get_user_data(generated_user)
        user = DeveloperUser.objects.create(**user_data)

        assert user.type == "DEVELOPER"


    def test_single_student_user_object_creation(self):
        generated_user = StudentUserFactory.build()
        user_data = get_user_data(generated_user)
        StudentUser.objects.create(**user_data)

        assert StudentUser.objects.count() == 1

    def test_created_student_user_has_specified_data(self):
        generated_user = StudentUserFactory.build()
        user_data = get_user_data(generated_user)
        user = StudentUser.objects.create(**user_data)

        assert user.username == generated_user.username

    def test_type_of_created_student_user(self):
        generated_user = StudentUserFactory.build()
        user_data = get_user_data(generated_user)
        user = StudentUser.objects.create(**user_data)

        assert user.type == "STUDENT"