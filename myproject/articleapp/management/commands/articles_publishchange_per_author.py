from django.core.management.base import BaseCommand
from articleapp.models import Article, Author
from datetime import datetime


class Command(BaseCommand):
    help = "Publish or Unpublish of Article per author's name"

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='author name')

    def handle(self, *args, **kwargs):
        author_name = kwargs['first_name']
        author = Author.objects.filter(first_name=author_name).first()
        articles = Article.objects.filter(author=author)
        for article in articles:
            if article.is_published == False:
                z = datetime.now()
                article.is_published = True
                article.publication_date = z
                article.save()
                self.stdout.write(f'{article} has been published on {z}')
            else: 
                article.is_published = False
                article.save()
                self.stdout.write(f'{article} has been unpublished')