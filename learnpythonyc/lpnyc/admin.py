from django.contrib import admin
from lpnyc.models import Person,IceCream
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','favorite_icecream']

@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    fields = ['name']