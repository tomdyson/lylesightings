from django.db import models
from location_field.models.plain import PlainLocationField


class Sighting(models.Model):
    sighter = models.CharField(max_length=200, help_text="Who saw the Lyle?")
    description = models.TextField()
    datetime = models.DateTimeField('date and time seen')
    url = models.CharField(max_length=250, verbose_name="URL", unique=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True, blank=True)

    def __str__(self):
        return '{sighter} in {city}'.format(sighter=self.sighter, city=self.city)
