# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0022_auto_20160529_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='owner',
        ),
    ]