# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-15 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disease_symptoms', models.TextField()),
                ('treatment_plan', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pest_symptoms', models.TextField()),
                ('treatment_plan', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Disease')),
                ('pest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pest')),
            ],
        ),
    ]
