from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory import Sequence
from ..models import DeveloperUser, StudentUser


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