# Generated by Django 5.0 on 2023-12-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_order_delivery_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
