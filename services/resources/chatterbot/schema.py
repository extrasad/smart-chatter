import typing

import graphene
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.ext.django_chatterbot import settings


class Message(graphene.ObjectType):
    """Type for message response."""

    response = graphene.String()


class Query:
    message = graphene.Field(Message, message=graphene.String(required=True))

    def resolve_message(self, info: typing.Dict, message: str) -> Message:
        """Respond message from an user for a given chatbot."""

        bot = ChatBot(**settings.CHATTERBOT)
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train(
            "chatterbot.corpus.english",
            "core.trainer_data.custom",
            "chatterbot.corpus.spanish",
            "core.trainer_data.feelings",
        )
        response = bot.get_response(message)
        response_data = response.serialize()
        date = response_data["created_at"].strftime("%Y-%m-%d %H:%M:%S")
        response_data.update({"created_at": date})
        return Message(response=response_data)
