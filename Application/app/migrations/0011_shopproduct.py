# Generated by Django 3.2.4 on 2021-06-16 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_shop_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('pesticide', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.pesticide')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.shop')),
            ],
        ),
    ]