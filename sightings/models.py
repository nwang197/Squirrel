from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    X = models.DecimalField(
            max_digits=20,
            decimal_places=15,
            help_text=_('Longitude'),
            null = True,)
    Y = models.DecimalField(
            max_digits=20,
            decimal_places=15,
            help_text=_('Latitude'),
            null=True,)
    Unique_Squirrel_ID = models.CharField(
            help_text=_('Unique Squirrel ID'),
            max_length=15,
            primary_key=True,)
   

#    Hectare = models.CharField(
#            help_text=_('Hectare'),
#            max_length = 4,
#            null = True,
#            default = None,
#            )

                                    

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
#    S_number = models.CharField(
#            help_text = _('Hectare Squirrel Number'),
#            max_length = 10,
#            null =True,)
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
                (CINNAMMON, 'Cinnammon'),
                (BLANK, ''),
                ),
            default = BLANK,
            max_length = 10,
            null=True,
            blank=True,  )                                                            
    Above_Ground = 'Above Ground'
    Ground_Plane = 'Ground Plane'
    BLANK = ''
    Location = models.CharField(
            help_text=_('Location'),
            choices = (
                        (Above_Ground, 'Above Ground'),
                        (Ground_Plane, 'Ground Plane'),
                        (BLANK, ''),
                       ),
            default = BLANK,
            max_length = 20,
            null = True,
            blank = True,)

                                                                                                                    
    Specific_Location = models.CharField(
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
    Tail_Flags=models.BooleanField(null=True)
    Tail_Twitches=models.BooleanField(null=True)
    Approaches=models.BooleanField(null=True) 
    Indifferent=models.BooleanField(null=True)  
    Runs_From=models.BooleanField(null=True)                                                                                                                                                            
    def __str__(self):
        return self.Unique_Squirrel_ID 
                                                                                                                                                                                            
