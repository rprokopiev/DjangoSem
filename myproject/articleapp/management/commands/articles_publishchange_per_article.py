from django.core.management.base import BaseCommand
from articleapp.models import Article, Author
from datetime import datetime


class Command(BaseCommand):
    help = "Publish/Unbublish Article per ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='article id')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        article = Article.objects.filter(pk=pk).first()
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