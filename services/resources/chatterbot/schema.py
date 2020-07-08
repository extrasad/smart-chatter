import graphene
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.ext.django_chatterbot import settings


class Conversation(graphene.ObjectType):
    name = graphene.String()


class Message(graphene.ObjectType):
    response = graphene.String()


class Query:
    conversation = graphene.Field(Conversation)
    message = graphene.Field(Message, message=graphene.String(required=True))

    def resolve_conversation(self, info):
        bot = ChatBot(**settings.CHATTERBOT)
        return Conversation(name=bot.name)

    def resolve_message(self, info, message):
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
