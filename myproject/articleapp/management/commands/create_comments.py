from django.core.management.base import BaseCommand
from articleapp.models import Article, Author, Comment
from django.utils import lorem_ipsum
from random import choice


class Command(BaseCommand):
    help = 'Create articles'
    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        articles = Article.objects.all()
        for i in range(1, 10):
            comment = Comment(
                author = choice(authors),
                article = choice(articles),
                content = "\n".join(lorem_ipsum.paragraphs(1, common=False)))
            comment.save()
            self.stdout.write(f'{comment}')