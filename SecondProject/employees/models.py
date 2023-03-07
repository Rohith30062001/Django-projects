from django.db import models

# Create your models here.
class Bookings(models.Model):
    destnation = models.CharField(max_length = 100)
    tripDate = models.DateField(max_length=20)
    bookingDate = models.DateField(max_length=20)
    userName = models.CharField(max_length=100)
    price = models.IntegerField(null = True)

class Test(models.Model):
    userName = models.ForeignKey(
        "Bookings", on_delete=models.CASCADE)

class Favorite_places(models.Model):
    picture = models.ImageField()
    price = models.IntegerField()
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    quotation = models.CharField(max_length=100, null=True)
    
