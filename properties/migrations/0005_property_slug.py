# Generated by Django 2.1.4 on 2019-01-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20181225_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
