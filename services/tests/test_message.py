from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from graphene.test import Client
from services.resources.schema import schema


class MessageTestCase(APITestCase):
    def test_sent_message(self):
        """
        Ensure we can send a message
        """
        data = {"text": "Hello"}
        response = self.client.post("/api/v1/message", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sent_message_graphql(self):
        """
        Ensure we can send a message in graphql api
        """
        client = Client(schema)
        query = """
        {
          message(message:"How are you") {
            response
          }
        }
        """
        executed = client.execute(query)
        self.assertTrue("text" in executed["data"]["message"]["response"])
