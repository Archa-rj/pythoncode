from django.db import models

# Create your models here.
from django.db import models

from django.db import models


# class District(models.Model):
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name
#
#
# class City(models.Model):
#     country = models.ForeignKey(District, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=124)
#     country = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
#
#     def __str__(self):
#         return self.name