from django.db import models


def example_func():
    return ["1", "faf", "ad"]


class Child(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(default=18)
    email = models.EmailField(default=255, unique=True)
    fav_toy = models.CharField(max_length=255, blank=False, default="")