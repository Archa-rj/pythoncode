#
from django.db import models


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Office(models.Model):
    district= models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    district= models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name