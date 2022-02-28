from django.contrib import admin
from Inventory.models import inventories, TruckExpense
# Register your models here.

admin.site.register(inventories)
admin.site.register(TruckExpense)