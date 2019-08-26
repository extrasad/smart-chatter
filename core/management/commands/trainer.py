from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Train for bot'

    def add_arguments(self, parser):
        parser.add_argument('times', nargs='+', type=int)

    def handle(self, *args, **options):
        times= options['times'][0]
        chatbot = ChatBot(**settings.CHATTERBOT)
        for i in range(0,times):
            trainer = ChatterBotCorpusTrainer(chatbot)

            trainer.train(
                "chatterbot.corpus.english",
                "core.trainer_data.custom"
            )
            # Get a response to the input text 'I would like to book a flight.'
            response1 = chatbot.get_response('Hello')
            response2 = chatbot.get_response('you are into videogames')
            self.stdout.write(self.style.SUCCESS(response2))