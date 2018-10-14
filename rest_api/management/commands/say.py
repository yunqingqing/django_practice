from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Displays current time'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str,
                            help='people name')
        parser.add_argument('-w', '--word', type=str,
                            help='words says', )

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        word = kwargs['word']
        self.stdout.write("{} say {}".format(name, word))

        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
