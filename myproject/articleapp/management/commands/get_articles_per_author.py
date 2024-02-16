from django.core.management.base import BaseCommand
from articleapp.models import Article, Author


class Command(BaseCommand):
    help = 'Search all articles of the author'

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='author name')

    def handle(self, *args, **kwargs):
        author_name = kwargs['first_name']
        author = Author.objects.filter(first_name=author_name).first()
        articles = Article.objects.filter(author=author)
        for article in articles:
            self.stdout.write(f'{article}')