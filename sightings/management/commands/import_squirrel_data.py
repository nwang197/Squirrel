import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
from datetime import date
from dateutil import parser

class Command(BaseCommand):
    help = 'Import Central Park Squirrel Census Data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            squirell_data = list(reader)

            for item in squirrel_data:
                s = Squirrel(
                    X=item['X'],
                    Y=item['Y'],
                    Unique_Squirrel_ID=item['Unique Squirrel ID'],
                    Shift=item['Shift'],
                    Date=datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]),int(item['Date'][2:4])),
                    Age=item['Age'],
                    Primary_Fur_Color=item['Primary Fur Color'],
                    Location = item['Location'],
                    Specific_location = item['Specific Location'],
                    Running=item['Running'].upper(),
                    Chasing=item['Chasing'].upper(),
                    Climbing=item['Climbing'].upper(),
                    Eating=item['Eating'].upper(),
                    Foraging=item['Foraging'].upper(),
                    Other_activities=item['Other Activities'],
                    Kuks=item['Kuks'].upper(),
                    Quaas=item['Quaas'].upper(),
                    Moans=item['Moans'].upper(),
                    Tail_flags=item['Tail flags'].upper(),
                    Tail_twitches=item['Tail twitches'].upper(),
                    Approaches=item['Approaches'].upper(),
                    Indifferent=item['Indifferent'].upper(),
                    Runs_from=item['Runs from'].upper(),
                    )
                s.save()

                






