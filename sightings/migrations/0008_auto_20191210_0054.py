# Generated by Django 2.2.7 on 2019-12-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0007_auto_20191210_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('', '')], default='', help_text='Primary Fur Color', max_length=10),
        ),
    ]
