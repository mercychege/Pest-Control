# Generated by Django 3.2.4 on 2021-06-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_disease_pesticide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]
