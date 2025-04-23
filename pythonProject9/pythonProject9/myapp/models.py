from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, default='')
    price = models.IntegerField()

    def __str__(self):
        return self.name
