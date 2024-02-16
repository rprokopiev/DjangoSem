from django.core.management.base import BaseCommand
from articleapp.models import Article, Comment


class Command(BaseCommand):
    help = "Get all Comments per Article title"

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Article title')

    def handle(self, *args, **kwargs):
        title = kwargs['title']
        article = Article.objects.filter(title=title).first()
        comments = Comment.objects.filter(article=article)
        for comment in comments:
            self.stdout.write(f'{comment}')