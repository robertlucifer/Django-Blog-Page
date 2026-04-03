from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This is used to populate the values"

    def handle(self, *args, **options):

        Category.objects.all().delete()

        categories = ['Sport','Techonology','Science','Arts','Yoga']
        for cata_name in categories:
            Category.objects.create(name = cata_name)

        self.stdout.write(self.style.SUCCESS("Completed Successfully"))