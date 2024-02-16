from django.core.management.base import BaseCommand, CommandParser
from articleapp.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Get all Comments per author's name"

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='author name')

    def handle(self, *args, **kwargs):
        author_name = kwargs['first_name']
        author = Author.objects.filter(first_name=author_name).first()
        comments = Comment.objects.filter(author=author)
        for comment in comments:
            self.stdout.write(f'{comment}')