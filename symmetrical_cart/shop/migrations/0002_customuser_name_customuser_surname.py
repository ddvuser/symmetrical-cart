# Generated by Django 5.0 on 2023-12-04 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='surname',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
