from django.db import models

class First(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)