# Generated by Django 4.2.3 on 2023-08-01 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spareApp', '0003_sales'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
    ]
