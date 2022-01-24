# Generated by Django 3.2.9 on 2022-01-08 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Clearance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clear',
            name='created_at',
        ),
        migrations.AddField(
            model_name='clear',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]