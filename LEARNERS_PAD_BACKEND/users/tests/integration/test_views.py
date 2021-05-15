import factory
from ..factories import DeveloperUserFactory
from ..utils import get_user_data
import pytest
from rest_framework.request import Request
from rest_framework.response import Response

pytestmark = pytest.mark.django_db


class TestDeveloperUserAPIViews:

    def test_developer_user_creation_view(self):
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory
        )

