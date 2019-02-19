from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32)
    dob = models.CharField(max_length=256)
    email = models.CharField(max_length=30)
    phone_no = models.IntegerField()
