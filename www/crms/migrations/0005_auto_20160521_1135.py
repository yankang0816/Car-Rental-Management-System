# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 03:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crms', '0004_auto_20160521_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.TextField(max_length=50)),
                ('daily_rental', models.DecimalField(decimal_places=2, max_digits=5)),
                ('time', models.DurationField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='alipay',
            field=models.ImageField(default='/home/peter/Assignment/SE-305-System analysis and design/project/mysite/images/generic_alipay_photo.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='car_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='drive_license',
            field=models.ImageField(default='/home/peter/Assignment/SE-305-System analysis and design/project/mysite/static/images/generic_drive_license_photo.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]