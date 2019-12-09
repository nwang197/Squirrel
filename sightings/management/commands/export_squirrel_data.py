import csv, sys
from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Export Squirrel Data as a CSV File'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path to the export file')

    def handle(self, path, **options):
        csvfields = Squirrel._meta.fields
        fieldname = [field.name for field in csvfields]
        with open(path, 'w', newline='') as exportfile:
            export = csv.writer(exportfile, quoting=csv.QUOTE_ALL)
            export.writerow(fieldname)
            for item in Squirrel.objects.all():
                export.writerow([getattr(item, fn) for fn in fieldname])
        print('Exporting Data Succeeded')


