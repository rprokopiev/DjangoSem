from django.core.management.base import BaseCommand
from articleapp.models import Author
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = 'Create Authors'

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            author = Author(
                first_name = f'{i}-Name',
                last_name = f'{i}-LastName',
                email = f'{i}email@mail.com',
                biography = lorem_ipsum.paragraphs(2),
                birth_date = f'196{i}-0{i}-1{i}')
            author.save()
            self.stdout.write(f'{author}')