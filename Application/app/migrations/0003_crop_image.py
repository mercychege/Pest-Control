# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-15 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210615_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images/'),
        ),
    ]
