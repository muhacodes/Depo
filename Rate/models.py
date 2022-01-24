from django.db import models

# Create your models here.

class Rate(models.Model):
    local_currency      = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    dollars             = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    rate                = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    created_at  		= models.DateField(auto_now_add=True)








    