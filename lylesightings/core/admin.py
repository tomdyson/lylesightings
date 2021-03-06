from django.contrib import admin

# Register your models here.
from core.models import Sighting, Spotter

class SightingAdmin(admin.ModelAdmin):
    list_filter = (['spotter'])
    list_display = ('description', 'datetime')

admin.site.site_header = "Lylesightings Administration"
admin.site.index_title = ""
admin.site.register(Sighting, SightingAdmin)
admin.site.register(Spotter)