from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient


class MessageTestCase(APITestCase):
    def test_sent_message(self):
        """
        Ensure we can sent a message
        """
        data = {"text": "Hello"}
        response = self.client.post("/api/v1/message", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
