# Generated by Django 2.1.4 on 2018-12-23 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20181221_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
