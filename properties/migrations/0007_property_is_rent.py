# Generated by Django 2.1.4 on 2019-03-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20190117_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_rent',
            field=models.BooleanField(default=False),
        ),
    ]
