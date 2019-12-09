import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import datetime

class Command(BaseCommand):
    help = 'Import Central Park Squirrel Census Data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            squirrel_data = list(reader)

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
                    Specific_Location = item['Specific Location'],
                    Running=item['Running'].lower().capitalize(),
                    Chasing=item['Chasing'].lower().capitalize(),
                    Climbing=item['Climbing'].lower().capitalize(),
                    Eating=item['Eating'].lower().capitalize(),
                    Foraging=item['Foraging'].lower().capitalize(),
                    Other_Activities=item['Other Activities'],
                    Kuks=item['Kuks'].lower().capitalize(),
                    Quaas=item['Quaas'].lower().capitalize(),
                    Moans=item['Moans'].lower().capitalize(),
                    Tail_Flags=item['Tail flags'].lower().capitalize(),
                    Tail_Twitches=item['Tail twitches'].lower().capitalize(),
                    Approaches=item['Approaches'].lower().capitalize(),
                    Indifferent=item['Indifferent'].lower().capitalize(),
                    Runs_From=item['Runs from'].lower().capitalize(),
                    )
                s.save()
        print('Importing Data Succeeded') 

                






