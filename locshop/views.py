from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr,Point
from django.contrib.gis.db.models.functions import Distance
from .models import Loc

#define user coordinate
longitude = -7.255880
latitude = 112.737778

user_loc = Point(longitude,latitude,srid=4326)

class Home(generic.ListView):
    model = Loc
    context_object_name = 'locshop'
    queryset = Loc.objects.annotate(distance=Distance('location',user_loc)).order_by('distance')[0:10]
    template_name = 'locshop/index.html'
