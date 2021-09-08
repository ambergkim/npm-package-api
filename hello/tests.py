from django.test import TestCase


class packageHealthViewTests(TestCase):
    def test_package_health_view(self):
        """
        Tests getting package health information
        """
        response = self.client.get("/package/health/dummy/0.9")

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            {
                "name": "dummy",
                "version": "0.9",
                "license": "MIT",
                "vulnerabilities": [
                    {
                        "id": "v2017-001",
                        "description": "this is a dummy cve",
                        "created": "2017-09-04T21:03:04Z",
                    }
                ],
            },
        )


class packageViewTests(TestCase):
    def test_package_view(self):
        """
        Test getting package info from npm
        """
        response = self.client.get("/package/releases/jsonwebtoken")

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding="utf8"),
            {
                "name": "jsonwebtoken",
                "latest": "8.5.1",
                "releases": [
                    "0.1.0",
                    "0.2.0",
                    "0.3.0",
                    "0.4.0",
                    "0.4.1",
                    "1.0.0",
                    "1.0.2",
                    "1.1.0",
                    "1.1.1",
                    "1.1.2",
                    "1.2.0",
                    "1.3.0",
                    "2.0.0",
                    "3.0.0",
                    "3.1.0",
                    "3.1.1",
                    "3.2.0",
                    "3.2.1",
                    "3.2.2",
                    "4.0.0",
                    "4.1.0",
                    "4.2.0",
                    "4.2.1",
                    "4.2.2",
                    "5.0.0",
                    "5.0.1",
                    "5.0.2",
                    "5.0.3",
                    "5.0.4",
                    "5.0.5",
                    "5.1.0",
                    "5.2.0",
                    "5.3.1",
                    "5.4.0",
                    "5.4.1",
                    "5.5.0",
                    "5.5.1",
                    "5.5.2",
                    "5.5.3",
                    "5.5.4",
                    "5.6.0",
                    "5.6.2",
                    "5.7.0",
                    "6.0.0",
                    "6.0.1",
                    "6.1.0",
                    "6.1.1",
                    "6.1.2",
                    "6.2.0",
                    "7.0.0",
                    "7.0.1",
                    "7.1.0",
                    "7.1.1",
                    "7.1.3",
                    "7.1.5",
                    "7.1.6",
                    "7.1.7",
                    "7.1.8",
                    "7.1.9",
                    "7.1.10",
                    "7.2.0",
                    "7.2.1",
                    "7.3.0",
                    "7.4.0",
                    "7.4.1",
                    "7.4.2",
                    "7.4.3",
                    "8.0.0",
                    "8.0.1",
                    "8.1.0",
                    "8.1.1",
                    "8.2.0",
                    "8.2.1",
                    "8.2.2",
                    "8.3.0",
                    "8.4.0",
                    "8.5.0",
                    "8.5.1",
                ],
            },
        )
