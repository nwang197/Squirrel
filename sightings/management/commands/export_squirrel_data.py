import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'Export Squirrel Data as a CSV File'

    def handle(self, *args, **options):
        with open 

