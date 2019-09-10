from django.db import models

# Create your models here.

class IceCream(models.Model):
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    favorite_icecream = models.ForeignKey(IceCream, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


