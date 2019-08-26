from django.core.management.base import BaseCommand, CommandError
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer

class Command(BaseCommand):
    help = 'Train for bot'

    def add_arguments(self, parser):
        parser.add_argument('times', nargs='+', type=int)

    def handle(self, *args, **options):
        times= options['times'][0]
        chatbot = ChatBot(**settings.CHATTERBOT)
        for i in range(0,times):
            trainer = ListTrainer(chatbot)
            
            trainer.train([
                "you are into videogames?"
                "A couple of them",
                "What game do you like",
                "I like to play WoW",
                "What do you think about dota2",
                "That game sucks, i don't like at all"      
            ])

            # Get a response to the input text 'I would like to book a flight.'
            response = chatbot.get_response('What game do you like')
            self.stdout.write(self.style.SUCCESS(response))