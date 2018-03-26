from django.contrib import admin

# Register your models here.
from core.models import Sighting, Spotter

class SightingAdmin(admin.ModelAdmin):
    list_filter = (['spotter'])

admin.site.register(Sighting, SightingAdmin)
admin.site.register(Spotter)