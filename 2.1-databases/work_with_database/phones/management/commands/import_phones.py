import csv

from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            add_phones = Phone(id=phone['id'], name=phone['name'], price=phone['price'], image=phone['image'],
                               release_date=phone['release_date'], lte_exists=phone['lte_exists'],
                               slug=slugify(phone['name']))
            add_phones.save()
            print(f'Телефон {add_phones.name} добавлен')
