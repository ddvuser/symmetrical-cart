# Generated by Django 5.0 on 2023-12-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_customuser_phone_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
