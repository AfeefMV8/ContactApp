from django.db import models

# Create your models here.

class registration(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    secretpassword = models.CharField(max_length=100)

class contacts(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)