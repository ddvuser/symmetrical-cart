# Generated by Django 5.0 on 2023-12-17 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_order_receiver_name_order_receiver_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='release',
            field=models.DateField(default=datetime.date(2023, 11, 19)),
            preserve_default=False,
        ),
    ]