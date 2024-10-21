from django.db import models
from django.core.validators import validate_email

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,validators=[validate_email])
    age = models.IntegerField()
    password = models.CharField(max_length=6)
    mark=models.CharField(max_length=100,default='00')
    