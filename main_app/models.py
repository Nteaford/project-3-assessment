from django.db import models
from django.forms import CharField

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=100),
    quantity = models.IntegerField(),
    