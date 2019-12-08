from django.db import models
from django.utils.translation import gettext as _


<<<<<<< HEAD
class Squirrel(models.Model):
    X = models.FloatField(
            help_text=_('X'),
            null = True,)
    Y = models.FloatField(
            help_text=_('Y'),
            null=True,)
    Unique_Squirrel_ID = models.CharField(
            help_text=_('Unique Squirrel ID'),
            max_length=15,
            primary_key=True,)
    def __str__(self):
          return self.Unique_Squirrel_ID
    Hectare = models.CharField(
            help_text=_('Hectare'),
            max_length = 4,
            null = True,)
                                    

    AM = 'AM'
    PM = 'PM'
    Shift = models.CharField(
            help_text = _('Shift'),
            choices = ((AM,'AM'),
                      (PM,'PM'),),
            default =AM,
            max_length = 2,
            null = True,)
    Date = models.DateField(
            help_text=_('Date'),
            null = True,)
    S_number = models.CharField(
            help_text = _('Hectare Squirrel Number'),
            max_length = 10,
            null =True,)
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'
    BLANK = ''
                                                                        
    Age = models.CharField(
            help_text=_('Age'),
            choices = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (UNKNOWN, 'Unknown'),
            (BLANK, ''),),
            default = BLANK,
            max_length=12,
            null=True,
            blank=True,
            )

                                                                                
    GRAY = 'Gray'
    BLACK = 'Black'
    CINNAMMON = 'Cinnammon'
    BLANK = ''

    Primary_Fur_Color = models.CharField(
            help_text=_('Primary Fur Color'),
            choices = (
                (GRAY, 'Gray'),
                (BLACK, 'Black'),
                (CINNAMMON, 'Cinnammon'),                                                                                                                                           (BLANK, ''), ),
            default = BLANK,
            max_length = 10,
            null=True,
            blank=True,  )                                                                                                                                              AG = 'Above Ground'
    GP = 'Ground Plane'
    BLANK = ''
    Loc = models.CharField(
            help_text=_('Location'),
            choices = (
                        (AG, 'Above Ground'),
                        (GP, 'Ground Plane'),
                        (BLANK, ''),),
            default = BLANK,
            max_length = 20,
            null = True,
            blank = True,)

                                                                                                                    
    Spe_Loc = models.CharField(
            help_text=_('Specific Location'),
            max_length = 100,
            null = True,
            blank = True,)
                                                                                                                        
    Running=models.BooleanField(null=True)
    Chasing=models.BooleanField(null=True)
    Climbing=models.BooleanField(null=True)
    Eating=models.BooleanField(null=True)
    Foraging=models.BooleanField(null=True)
    Other_Activities = models.CharField(
            help_text=_('Other Activities'),
            max_length=200,
            null=True,
            blank=True,
            )
    Kuks=models.BooleanField(null=True)
    Quaas=models.BooleanField(null=True)
    Moans=models.BooleanField(null=True)
    Tail_flags=models.BooleanField(null=True)
    Tail_twitches=models.BooleanField(null=True)
    Approaches=models.BooleanField(null=True)                                                                                                                           Indifferent=models.BooleanField(null=True)                                                                                                                          Run_from=models.BooleanField(null=True)
                                                                                                                                                                                    
                                                                                                                                                                                        
                                                                                                                                                                                            
=======
>>>>>>> b5cfe17028b1cc358e9120011c4d3a230c661751
# Create your models here.
