from django.db import models

# Create your models here.
class products(models.Model):
    name                = models.CharField(max_length=50)
    description         = models.TextField(max_length=1000, null=True, blank=True)
    quantity            = models.SmallIntegerField()
    cost_price			= models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Cost Price")
    selling_price		= models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Selling Price")
    available           = models.BooleanField(default=True)
    created_at  		= models.DateField(verbose_name="Date")
    updated_at  		= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
