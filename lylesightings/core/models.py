from django.db import models
from location_field.models.plain import PlainLocationField


class Spotter(models.Model):
    name = models.CharField(max_length=200)
    instagram_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Sighting(models.Model):
    spotter = models.ForeignKey('Spotter', null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    datetime = models.DateTimeField('date and time seen')
    photo = models.ImageField(upload_to='sighting-photos', null=True)
    url = models.CharField(max_length=250, verbose_name="URL", unique=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True,
                                  blank=True)

    def lat(self):
        if self.location and len(self.location):
            return self.location.split(',')[0]

    def lon(self):
        if self.location and len(self.location):
            return self.location.split(',')[1]

    def __str__(self):
        return '{sighter} in {city}'.format(sighter=self.spotter.name,
                                            city=self.city)
