from django.contrib import admin
from vdata.models import Publisher,Platform,Genre,Videogame

# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ['name']

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    fields = ['name']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ['name']

@admin.register(Videogame)
class VideogameAdmin(admin.ModelAdmin):
    fields = ['name', 'platform', 'released', 'genre', 'publisher', 'na_sales']