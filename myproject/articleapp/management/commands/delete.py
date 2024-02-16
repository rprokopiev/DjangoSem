from django.core.management.base import BaseCommand
from articleapp.models import Article, Author, Comment

class Command(BaseCommand):
    help = 'Delete data from all data base tables'

    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        Comment.objects.all().delete()
        Article.objects.all().delete()