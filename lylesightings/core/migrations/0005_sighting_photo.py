# Generated by Django 2.0.3 on 2018-03-22 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180119_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]