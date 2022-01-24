from django.db import models
from Inventory.models import inventories
# Create your models here.

class clear(models.Model):
    Date  		            = models.DateField()
    inventory               = models.ForeignKey(inventories, on_delete=models.CASCADE)
    agent_name              = models.CharField(max_length=250)
    amount			        = models.DecimalField(max_digits=10, decimal_places=0)
    balance			        = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.agent_name