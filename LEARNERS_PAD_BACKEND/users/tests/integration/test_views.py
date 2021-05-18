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
        retrieve_url = reverse("users:developer-user-detail", kwargs={"uuid": generated_user.uuid})

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
        retrieve_url = reverse("users:student-user-detail", kwargs={"uuid": generated_user.uuid})

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


class TestUserLoginView:

    def test_developer_user_login(self, api_client):
        generated_user = DeveloperUserFactory.build()
        user_data = get_user_data(generated_user)

        # create developer user
        create_url = reverse("users:developer-user-create")
        create_response = api_client.post(
            create_url,
            data=user_data,
        )

        # log user in if create is successful
        if create_response.status_code == 200:
            login_url = reverse("users:login")
            login_response = api_client.post(
                login_url,
                data = {
                    "username": user_data["username"],
                    "password": user_data["password"],
                }
            )

            assert login_response == 200
            assert json.loads(login_response.content)["token"]
            assert json.loads(login_response.content)["user_retrieve_url"]
            assert json.loads(login_response.content)["message"] == "Login successful"
            assert "developer" in json.loads(login_response.content)["user_retrieve_url"]

    def test_student_user_login(self, api_client):
        generated_user = StudentUserFactory.build()
        user_data = get_user_data(generated_user)

        # create developer user
        create_url = reverse("users:student-user-create")
        create_response = api_client.post(
            create_url,
            data=user_data,
        )

        # log user in if create is successful
        if create_response.status_code == 200:
            login_url = reverse("users:login")
            login_response = api_client.post(
                login_url,
                data = {
                    "username": user_data["username"],
                    "password": user_data["password"],
                }
            )

            assert login_response == 200
            assert json.loads(login_response.content)["token"]
            assert json.loads(login_response.content)["user_retrieve_url"]
            assert json.loads(login_response.content)["message"] == "Login successful"
            assert "student" in json.loads(login_response.content)["user_retrieve_url"]