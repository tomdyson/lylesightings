# Generated by Django 2.0.3 on 2018-03-25 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_sighting_spotter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='sighter',
        ),
    ]
