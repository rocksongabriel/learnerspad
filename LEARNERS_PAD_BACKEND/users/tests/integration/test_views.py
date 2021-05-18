from django.http import response
import factory
from ..factories import DeveloperUserFactory, StudentUserFactory
import pytest
from django.urls import reverse
import json
from users.tests.utils import get_user_data

pytestmark = pytest.mark.django_db


class TestDeveloperUserAPIViews:

    def test_developer_user_creation(self, api_client):
        json_data = factory.build(
            dict,
            FACTORY_CLASS = DeveloperUserFactory
        )

        url = reverse("users:developer-user-create")

        res = api_client.post(
            url,
            data=json_data
        )

        content = json.loads(res.content)

        assert res.status_code == 201
        assert content["message"] == "User {} has been created successfully".format(json_data["username"])

    def test_developer_user_retrieve(self, api_client):
        generated_user = DeveloperUserFactory.build()

        user_data = get_user_data(generated_user)

        create_url = reverse("users:developer-user-create")
        retrieve_url = reverse("users:developer-user-detail", kwargs={"username": generated_user.username})

        create_response = api_client.post(
            create_url,
            data=user_data
        )

        if create_response.status_code == 200:
            retrieve_response = api_client.get(
                retrieve_url
            )

            content = json.loads(retrieve_response.content)

            assert retrieve_response.status_code == 200
            assert content["username"] == generated_user.username

    def test_developer_login_view(self, api_client):
        generated_user = DeveloperUserFactory.create()
        user_data = get_user_data(generated_user)

        # create the user
        create_user_url = reverse("users:student-user-login")
        create_res = api_client.post(
            create_user_url,
            data = user_data
        )

        if create_res.status_code == 200:
            login_url = reverse("users:developer-user-login")
            res = api_client.post(
                login_url,
                data={
                    "username": user_data["username"],
                    "password": user_data["password"],
                }
            )

            assert res.status_code == 200 # assert status code is 200
            assert json.loads(res.content)["token"]
            assert json.loads(res.content)["user_retrieve_url"]


class TestStudentUserAPIViews:

    def test_student_user_creation(self, api_client):
        json_data = factory.build(
            dict,
            FACTORY_CLASS = StudentUserFactory
        )

        url = reverse("users:student-user-create")

        res = api_client.post(
            url,
            data=json_data
        )

        content = json.loads(res.content)

        assert res.status_code == 201
        assert content["message"] == "User {} has been created successfully".format(json_data["username"])

    def test_student_user_retrieve(self, api_client):
        generated_user = StudentUserFactory.build()

        user_data = get_user_data(generated_user)

        create_url = reverse("users:student-user-create")
        retrieve_url = reverse("users:student-user-detail", kwargs={"username": generated_user.username})

        create_response = api_client.post(
            create_url,
            data=user_data
        )

        if create_response.status_code == 200:
            retrieve_response = api_client.get(
                retrieve_url
            )

            content = json.loads(retrieve_response.content)

            assert retrieve_response.status_code == 200
            assert content["username"] == generated_user.username

    def test_student_login_view(self, api_client):
        generated_user = StudentUserFactory.build()
        user_data = get_user_data(generated_user)

        # create the user
        create_user_url = reverse("users:student-user-login")
        create_res = api_client.post(
            create_user_url,
            data = user_data
        )

        if create_res.status_code == 200:
            # log the user in
            login_url = reverse("users:student-user-login")
            res = api_client.post(
                login_url,
                data={
                    "username": user_data["username"],
                    "password": user_data["password"],
                }
            )

            assert res.status_code == 200 # assert status code is 200
            assert json.loads(res.content)["token"]
            assert json.loads(res.content)["user_retrieve_url"]