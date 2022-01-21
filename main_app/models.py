from django.db import models
from django.forms import CharField

# Create your models here.
class Widget(models.Model):
    name = models.CharField(max_length=30),
    description = models.CharField(max_length=100),
    quantity = models.IntegerField(),

    def __str__(self):
        return self.name