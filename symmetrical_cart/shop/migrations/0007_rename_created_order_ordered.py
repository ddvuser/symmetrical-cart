# Generated by Django 5.0 on 2023-12-11 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_customer_order_user_remove_order_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created',
            new_name='ordered',
        ),
    ]