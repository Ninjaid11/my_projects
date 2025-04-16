from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Basket(models.Model):
    name = models.CharField(max_length=100)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name