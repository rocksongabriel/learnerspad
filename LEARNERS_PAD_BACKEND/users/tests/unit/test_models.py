import pytest
from ..factories import DeveloperUserFactory, StudentUserFactory
from ...models import DeveloperUser, StudentUser, DeveloperUserProfile, StudentUserProfile
from ..utils import get_user_data


pytestmark = pytest.mark.django_db

class TestUserObjectCreation:

    def test_single_developer_user_object_creation(self, developer_user):
        DeveloperUser.objects.create(**developer_user)
        assert DeveloperUser.objects.count() == 1

    def test_created_developer_user_has_specified_data(self, developer_user):
        user = DeveloperUser.objects.create(**developer_user)
        assert user.username == developer_user["username"]

    def test_type_of_created_developer_user(self, developer_user):
        user = DeveloperUser.objects.create(**developer_user)
        assert user.type == "DEVELOPER"


    def test_single_student_user_object_creation(self, student_user):
        StudentUser.objects.create(**student_user)
        assert StudentUser.objects.count() == 1

    def test_created_student_user_has_specified_data(self, student_user):
        user = StudentUser.objects.create(**student_user)
        assert user.username == student_user["username"]

    def test_type_of_created_student_user(self, student_user):
        user = StudentUser.objects.create(**student_user)
        assert user.type == "STUDENT"


class TestUserProfileCreation:
    """These tests test the creation of individual profiles for each user type"""

    def test_developer_user_profile_creation(self):
        """test the creation of a developer user profile"""
        generated_user = DeveloperUserFactory.build()

        user_data = get_user_data(generated_user)

        user = DeveloperUser.objects.create(**user_data)
        user.save() # On save, the post save signal will create an associated profile

        profile = DeveloperUserProfile.objects.get(user=user) # Try to get the profile associated with this user

        assert profile # assert the profile
        assert profile.user.username == generated_user.username

    def test_student_user_profile_creation(self):
        """test the creation of a student user profile"""
        generated_user = StudentUserFactory.build()

        user_data = get_user_data(generated_user)

        user = StudentUser.objects.create(**user_data)
        user.save()


        profile = StudentUserProfile.objects.get(user=user)

        assert profile
        assert profile.user.username == generated_user.username