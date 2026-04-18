from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from professionals.models import Professional


class ProfessionalAPITest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin", password="123456", is_staff=True
        )

        self.professional = Professional.objects.create(
            social_name="Maria",
            occupation="Fisioterapeuta",
            address="Rua A",
            contact="61999999999",
        )
        self.list_url = "/api/professionals/"
        self.detail_url = f"/api/professionals/{self.professional.id}/"
        self.client.force_authenticate(user=self.admin)

    # CREATE inválido
    def test_create_invalid_contact(self):
        data = {
            "social_name": "João",
            "occupation": "Médico",
            "address": "Rua B",
            "contact": "61",
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("contact", response.data["errors"])

    # VALIDAÇÃO GLOBAL
    def test_validate_errors(self):
        data = {
            "social_name": "maria",
            "occupation": "maria",
            "address": "Rua válida",
            "contact": "61985641340",
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("non_field_errors", response.data["errors"])

    # CREATE
    def test_create_professional(self):
        data = {
            "social_name": "João",
            "occupation": "Médico",
            "address": "Rua B",
            "contact": "61988888888",
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Professional.objects.count(), 2)

    # LIST
    def test_list_professionals(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["success"])

    # DETAIL
    def test_retrieve_professional(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["success"])

    # UPDATE
    def test_update_professional(self):
        data = {
            "social_name": "Maria Atualizada",
            "occupation": "Fisioterapeuta",
            "address": "Rua A",
            "contact": "61999999999",
        }

        response = self.client.put(self.detail_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["data"]["social_name"], "Maria Atualizada")

    # PATCH (parcial)
    def test_partial_update_professional(self):
        data = {"social_name": "Maria Patch"}

        response = self.client.patch(self.detail_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["data"]["social_name"], "Maria Patch")

    def test_partial_update_empty_address(self):
        data = {"address": ""}

        response = self.client.patch(self.detail_url, data)

        self.assertEqual(response.status_code, 400)
        self.assertIn("address", response.data["errors"])

    # DELETE
    def test_delete_professional(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Professional.objects.filter(id=self.professional.id).exists())
        self.assertTrue(response.data["success"])

    # DELETE BLOCKED
    def test_delete_professional_common_user_forbidden(self):
        user = User.objects.create_user(username="user", password="123456")

        self.client.force_authenticate(user=user)

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 403)
