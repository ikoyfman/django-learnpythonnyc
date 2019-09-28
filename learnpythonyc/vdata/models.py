from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Videogame(models.Model):
    name = models.CharField(max_length=80)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    released = models.IntegerField(null=True, blank=True)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    na_sales = models.DecimalField(decimal_places=2,max_digits=5, null=True)

    def __str__(self):
        return self.name


