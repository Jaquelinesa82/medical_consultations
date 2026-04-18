from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class JWTAuthenticationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="123456")

        self.protected_url = "/api/consultations/"
        self.token_url = "/api/token/"

    def test_access_without_token(self):
        response = self.client.get(self.protected_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_with_valid_token(self):
        token_response = self.client.post(
            self.token_url, {"username": "admin", "password": "123456"}
        )

        access = token_response.data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

        response = self.client.get(self.protected_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_with_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer token_fake")

        response = self.client.get(self.protected_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
