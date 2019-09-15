from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
from lpnyc.models import Person, IceCream

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now().strftime("%A %x %X")
    html = "<html><body>It is now {}.</body></html>".format(now)
    return HttpResponse(html)


def get_cat_fact(request):
    url = "https://catfact.ninja/facts"
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
    )
    data = response.json()
    data = data['data'][0]["fact"]
    html = "<html><body><h1>{}</h1></body></html>".format(data)
    return HttpResponse(html)

def people_view(request):
    people = Person.objects.all()
    return HttpResponse(people)

def ice_cream_view(request):
    ice_cream = IceCream.objects.all()
    return HttpResponse(ice_cream)