# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0021_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='car'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='daily_rental',
            field=models.PositiveIntegerField(),
        ),
    ]