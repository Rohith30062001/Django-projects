from django.db import models

# Create your models here.
class Bookings(models.Model):
    destnation = models.CharField(max_length = 100)
    tripDate = models.DateField(max_length=20)
    bookingDate = models.DateField(max_length=20)
    userName = models.CharField(max_length=100)

    
