from django.db import models
from Employee.models import Employee
# Create your models here.

class Salary(models.Model):
    employee                = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount			        = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  		    = models.DateField(verbose_name="Date")

    def __str__(self):
        return self.employee.name