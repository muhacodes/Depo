from os import name
from django.db import models

# Create your models here.

class ExpenseType(models.Model):
    name                = models.CharField(verbose_name="Expense Type",max_length=50)
    created_at  		= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Expense(models.Model):
    type                = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, null=True, blank=True)
    name                = models.CharField(verbose_name="Expense name",max_length=50, null=True, blank=True)
    description         = models.TextField(max_length=1000, null=True, blank=True)
    amount				= models.DecimalField(max_digits=7, decimal_places=0)
    created_at  		= models.DateField(auto_now_add=True)
    updated_at  		= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else self.type.name 