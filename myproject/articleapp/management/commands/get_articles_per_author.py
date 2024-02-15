from django.core.management.base import BaseCommand, CommandParser
from articleapp.models import Article, Author, Comment
from django.utils import lorem_ipsum
from random import choice


class Command(BaseCommand):
    help = 'Search all articles of the author'

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='author name')

    def handle(self, *args, **kwargs):
        author_name = kwargs['first_name']
        articles = Article.objects.filter(author=author_name)
        self.stdout.write(f'{articles}')