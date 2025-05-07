from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class MainProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)