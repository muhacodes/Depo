# Generated by Django 3.2.9 on 2022-01-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clearance', '0002_auto_20220108_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clear',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='clear',
            name='balance',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]