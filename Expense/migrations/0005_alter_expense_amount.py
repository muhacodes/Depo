# Generated by Django 3.2.9 on 2022-03-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0004_alter_expense_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=13),
        ),
    ]
