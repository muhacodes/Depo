# Generated by Django 3.2.9 on 2022-03-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0008_alter_expense_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensetype',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
