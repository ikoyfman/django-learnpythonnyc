from django.shortcuts import render
from vdata.models import Videogame
from rest_framework import viewsets
from vdata_api.serializers import VideogameSerializer

# Create your views here.

class VideogameViewSet(viewsets.ModelViewSet):
    queryset = Videogame.objects.all()
    serializer_class = VideogameSerializer