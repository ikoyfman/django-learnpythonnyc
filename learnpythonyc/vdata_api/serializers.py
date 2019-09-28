from django.contrib.auth.models import User, Group
from vdata.models import Videogame
from rest_framework import serializers

class VideogameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Videogame
        fields = ['name', 'platform', 'released', 'genre', 'publisher', 'na_sales']
        depth = 1