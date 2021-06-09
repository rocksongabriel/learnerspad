from django.db import models
from factory import Sequence
import factory
from factory import faker
from factory.django import DjangoModelFactory
from factory.faker import Faker
from users.tests.factories import StudentUserFactory

from ..models import Note


class NoteFactory(DjangoModelFactory):

    class Meta:
        model = Note

    # owner = factory.RelatedFactory(StudentUserFactory)
    owner = factory.SubFactory(StudentUserFactory)
    # title = factory.LazyAttribute(lambda x: faker.sentence(nb_words=20))
    # body = factory.LazyAttribute(lambda x: faker.sentence(nb_words=300))
    title = Faker("sentence")
    body = Faker("paragraph")
