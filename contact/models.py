from django.db import models

# Create your models here.
class FeedBack(models.Model):
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    Comments = models.TextField()

   