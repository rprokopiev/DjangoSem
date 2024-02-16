from django.core.management.base import BaseCommand
from randomapp.models import HeadsTailsResult
from random import randint, choice
from datetime import datetime


class Command(BaseCommand):
    help = 'Generates given amount of "throws", records resuls in dictionary'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='HeadsTails series')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        dict_result = {'Heads': 0, 'Tails': 0}
        for i in range(count):
            result = HeadsTailsResult(result=choice(['HEADS', 'TAILS']), time=datetime.now())
            result.save()
            if result.result == 'HEADS':
                dict_result['Heads'] += 1
            else:
                dict_result['Tails'] += 1
        self.stdout.write(f'{dict_result}')

