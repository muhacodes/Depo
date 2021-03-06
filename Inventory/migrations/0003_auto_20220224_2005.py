# Generated by Django 3.2.9 on 2022-02-24 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20220224_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckexpense',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckexpense',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
