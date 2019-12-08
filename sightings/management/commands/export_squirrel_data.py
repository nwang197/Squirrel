import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Export Squirrel Data as a CSV File'

    def handle(self, *args, **options):
        csvpath = args[0]
        csvfields = Squirrel._meta.fields
        with open(csvpath, 'w') as exportfile:
            export = csv.writer(exportfile)
            for item in Squirrel.objects.all():
                exportrow = [getattr(item, field.name) for field in csvfields]
                export.writerow(exportrow)
                exportfile.close()


