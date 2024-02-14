from django.core.management.base import BaseCommand
from articleapp.models import Article, Author
from django.utils import lorem_ipsum
from random import choice


class Command(BaseCommand):
    help = 'Create articles'
    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        for i in range(1, 10):
            article = Article(
                title = lorem_ipsum.words(5, common=False),
                content = "\n".join(lorem_ipsum.paragraphs(7, common=False)),
                publication_date = f'199{i}-0{i}-1{i}',
                author = choice(authors),
                category = choice(lorem_ipsum.WORDS))
            article.save()
            self.stdout.write(f'{article}')