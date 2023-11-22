from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient


class RegisterClientUserViewTest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(get_user_model())
        self.url = reverse('register-client')
        self.client = APIClient()
        self.valid_data = {
            "first_name": "test first name",
            "last_name": "test last name",
            "email": "valid-test-user@example.com",
            "password": "Pass123@#$",
            "fcm_token": "test-token"
        }
        self.invalid_data = {
            "invalid": "invalid"
        }

    @patch("core.api.v1.views.register_client_user_view."
           "RegisterUserService.register_client_user")
    def test_user_can_register_successfully_returns_201(
            self,
            register_client_service_mock
    ):
        register_client_service_mock.return_value = self.user
        response = self.client.post(
            self.url,
            data=self.valid_data
        )
        register_client_service_mock.assert_called_once_with(
            first_name=self.valid_data["first_name"],
            last_name=self.valid_data["last_name"],
            email=self.valid_data["email"],
            password=self.valid_data["password"],
            fcm_token=self.valid_data["fcm_token"]
        )
        self.assertEqual(response.status_code, 201)

    def test_invalid_serializer_returns_400_response(self):
        response = self.client.post(self.url, data=self.invalid_data)
        self.assertEqual(response.status_code, 400)
