
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


class ChatterMessage(generics.CreateAPIView):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """

        if 'text' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        response = self.chatterbot.get_response(request.data['text'])

        response_data = response.serialize()

        return Response(response_data, status=status.HTTP_200_OK)

class Conversation(generics.RetrieveAPIView):
    chatterbot = ChatBot(**settings.CHATTERBOT)
    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return Response({'name': self.chatterbot.name}, status=status.HTTP_200_OK)

    