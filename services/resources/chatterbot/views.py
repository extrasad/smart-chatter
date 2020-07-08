import typing

from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request


class ChatterMessage(generics.CreateAPIView):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)
    trainer = ChatterBotCorpusTrainer(chatterbot)
    trainer.train(
        "chatterbot.corpus.english",
        "core.trainer_data.custom",
        "core.trainer_data.feelings",
        "chatterbot.corpus.spanish",
    )

    def post(
        self, request: Request, *args: typing.Dict, **kwargs: typing.Dict
    ) -> Response:
        """
        Return a response to the statement in the posted data.
        * The JSON data should contain a 'text' attribute.
        """

        if "text" not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        response = self.chatterbot.get_response(request.data["text"])

        response_data = response.serialize()

        return Response(response_data, status=status.HTTP_200_OK)
