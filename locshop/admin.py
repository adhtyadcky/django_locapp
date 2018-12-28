from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin
from .models import Loc

@admin.register(Loc)
class LocAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
