from rest_framework.test import APITestCase

from consultations.models import Consultation
from professionals.models import Professional


class ConsultationAPITest(APITestCase):
    def setUp(self):
        self.professional = Professional.objects.create(
            social_name="Maria",
            occupation="Fisioterapeuta",
            address="Rua A",
            contact="61999999999",
        )

        self.consultation = Consultation.objects.create(
            professional=self.professional,
            patient_name="João",
            date="2026-04-20",
            time="10:00:00",
        )

        self.list_url = "/api/consultations/"
        self.detail_url = f"/api/consultations/{self.consultation.id}/"

    # Create
    def test_create_consultation(self):
        data = {
            "professional": self.professional.id,
            "patient_name": "ana",
            "date": "2026-04-21",
            "time": "11:00:00",
            "description": "Consulta inicial",
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Consultation.objects.count(), 2)

    # List
    def test_list_consultations(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["success"])
        self.assertEqual(len(response.data["data"]), 1)

    # Unique
    def test_unique_consultation(self):
        data = {
            "professional": self.professional.id,
            "patient_name": "ana",
            "date": "2026-04-20",
            "time": "10:00:00",
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, 400)

    # Detail
    def test_retrieve_consultation(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["success"])

    # Update (PUT)
    def test_update_consultation(self):
        data = {
            "professional": self.professional.id,
            "patient_name": "João Atualizado",
            "date": "2026-04-20",
            "time": "11:30:00",
        }

        response = self.client.put(self.detail_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["data"]["patient_name"], "João Atualizado")

    # PATCH (parcial)
    def test_partial_update_consultation(self):
        data = {"patient_name": "Joao Patch"}

        response = self.client.patch(self.detail_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["data"]["patient_name"], "Joao Patch")

    # Delete
    def test_delete_consultation(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Consultation.objects.filter(id=self.consultation.id).exists())
