# Generated by Django 4.2.3 on 2023-08-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareApp', '0005_rename_recieved_quantity_product_received_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
