from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from graphene.test import Client
from services.resources.schema import schema


class ConversationTestCase(APITestCase):
    def test_get_conversation(self):
        """
        Ensure we can get conversation
        """
        response = self.client.get("/api/v1/conversation")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
