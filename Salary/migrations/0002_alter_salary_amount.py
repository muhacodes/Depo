# Generated by Django 3.2.9 on 2022-03-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]