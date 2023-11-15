from django.db import models

# Create your models here.
class FinancialService(models.Model):
    desc=models.TextField()
    img=models.ImageField(upload_to='img')

    def __str__(self):
        return self.desc
