from factory import Sequence
from factory.django import DjangoModelFactory
from factory.faker import Faker

from ..models import (DeveloperUser, DeveloperUserProfile, StudentUser,
                      StudentUserProfile)


class DeveloperUserFactory(DjangoModelFactory):

    class Meta:
        model = DeveloperUser

    username = Sequence(lambda n: "dev%d" %n)
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    password = "testpass1234"


class StudentUserFactory(DjangoModelFactory):
    
    class Meta:
        model = StudentUser

    username = Sequence(lambda n: "devuser%d" %n)
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    password = "testpass1234"


class DeveloperUserProfileFactory(DjangoModelFactory):

    class Meta:
        model = DeveloperUserProfile

    bio = Faker("paragraph")


class StudentUserProfileFactory(DjangoModelFactory):

    class Meta:
        model = StudentUserProfile
    
    bio = Faker("paragraph")