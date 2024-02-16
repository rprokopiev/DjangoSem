from django.core.management.base import BaseCommand
from articleapp.models import Author, Article, Comment
from django.utils import lorem_ipsum
from random import randint, choice


class Command(BaseCommand):
    help = 'Create given amount of Authors'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="authors")


    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(count):
            if 0 < i < 10:
                n = i
            else: 
                n = 1
            author = Author(
                first_name = f'{i}-{randint(1,5)}{randint(1,5)}{randint(1,5)}-Name',
                last_name = f'{i}-{randint(1,5)}{randint(1,5)}{randint(1,5)}-LastName',
                email = f'{i}{randint(1,5)}{randint(1,5)}{randint(1,5)}-email@mail.com',
                biography = lorem_ipsum.paragraphs(2),
                birth_date = f'196{n}-0{n}-1{n}')
            author.save()
            self.stdout.write(f'{author}')

            for _ in range(randint(3,5)):
                article = Article(
                    title = lorem_ipsum.words(1, common=False),
                    content = "\n".join(lorem_ipsum.paragraphs(7, common=False)),
                    publication_date = f'199{n}-0{n}-1{n}',
                    author = author,
                    category = choice(lorem_ipsum.WORDS))
                article.save()
                self.stdout.write(f'{article}')

                for _ in range(randint(1, 3)):
                    comment = Comment(
                        author = author,
                        article = article,
                        content = "\n".join(lorem_ipsum.paragraphs(1, common=False)))
                    comment.save()
                    self.stdout.write(f'{comment}')
