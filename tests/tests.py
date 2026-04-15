from django.test import TestCase  # noqa: F401


class HealthCheck(TestCase):
    def test_health_check(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
