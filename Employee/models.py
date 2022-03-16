from django.db import models
from django.forms.widgets import Widget
from django.db.models.signals import post_save
# Create your models here.


class Employee(models.Model):
    name                = models.CharField(max_length=50)
    amount			    = models.DecimalField(max_digits=10, decimal_places=2)
    joined              = models.DateField()

    def __str__(self):
        return self.name
