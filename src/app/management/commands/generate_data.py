from django.core.management.base import BaseCommand
from app.models import Item
from random import randint
from faker import Faker

fake = Faker()

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for i in range(10):
        
            items = [
                Item(
                    name=fake.name(),
                    value=randint(1, 1000),
                    description=fake.text(),
                )
                for _ in range(10000) 
            ]
            Item.objects.bulk_create(items)
            self.stdout.write(self.style.SUCCESS("ЗАЕБИСЬ!"))
