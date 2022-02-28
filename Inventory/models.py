from django.db import models
from django.db.models.signals import post_save
from Product.models import products
# Create your models here.

class inventories(models.Model):
    name                = models.CharField(max_length=50)
    description         = models.TextField(max_length=1000, null=True, blank=True)
    quantity            = models.SmallIntegerField()
    cost_price			= models.DecimalField(max_digits=7, decimal_places=0, null=True, verbose_name="Cost Price")
    # selling_price		= models.DecimalField(max_digits=7, decimal_places=2, null=True, verbose_name="Selling Price")
    numberPlate         = models.CharField(max_length=7, null=True, blank=True)
    created_at  		= models.DateField(auto_now_add=True)
    updated_at  		= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TruckExpense(models.Model):
    Truck           = models.ForeignKey(inventories, on_delete=models.CASCADE)
    expense         = models.CharField(max_length=100)
    description     = models.CharField(max_length=2000, null=True, blank=True)
    amount			= models.DecimalField(max_digits=10, decimal_places=0, null=True)
    created_at  	= models.DateField(auto_now_add=True)
    updated_at  	= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense



def add_product(sender, instance, *args, **kwargs):
    obj = products(
        name=instance.name, 
        description=instance.description,
        quantity = instance.quantity,
        cost_price = instance.cost_price,
        created_at = instance.created_at

    )
    obj.save()
    print('saved')

post_save.connect(add_product, sender=inventories)