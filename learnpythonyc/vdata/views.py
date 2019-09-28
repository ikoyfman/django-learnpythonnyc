from django.shortcuts import render
from vdata.models import Videogame

# Create your views here.
def vdata_view(request):
    vdata = Videogame.objects.all()

    return render(request, 'vdata/vdata.html', context={'vdata':vdata})