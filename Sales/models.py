from django.db import models
from Product.models import products
from django.db.models.signals import post_save
# Create your models here.

class Sale(models.Model):
    product             = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity            = models.SmallIntegerField()
    selling_price		= models.DecimalField(max_digits=10, decimal_places=2, blank=True ,verbose_name="Selling Price")
    created_at  		= models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.product.name



def update_quantity(sender, instance, *args, **kwargs):
    id = instance.product.id
    product = products.objects.get(id=id)
    product.quantity = product.quantity - instance.quantity
    product.save()


post_save.connect(update_quantity, sender=Sale)