from django.shortcuts import render
import requests

# Create your views here.

from django.http import HttpResponse
import datetime


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