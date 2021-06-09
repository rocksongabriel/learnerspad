from notes.models import Note
import pytest
from notes.tests.factories import NoteFactory
from users.tests.factories import StudentUserFactory
from users.tests.utils import get_user_data
from users.models import StudentUser


pytestmark = pytest.mark.django_db

class TestNoteObjectCreation:

    def test_note_object_creation(self):
        generated_user = StudentUserFactory.build()
        user_data = get_user_data(generated_user)
        owner = StudentUser.objects.create(**user_data)

        generated_note = NoteFactory.build()
        data = {
            "title": generated_note.title,
            "owner": owner,
            "body": generated_note.body,
        }
        Note.objects.create(**data)

        assert Note.objects.count() == 1
