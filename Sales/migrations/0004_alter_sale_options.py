# Generated by Django 3.2.9 on 2022-03-20 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0003_alter_sale_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ['-created_at']},
        ),
    ]
