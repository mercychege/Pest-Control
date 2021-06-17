"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
# Crop Model which translates to crop table in the DB


class Crop(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    local_name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg',
                              blank=True, upload_to='images/')

    # date only when created, cant update this
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Pest Model which translates to pest table in the DB
class Pesticide(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg',
                              blank=True, upload_to='images/', unique=True)

    def __str__(self):
        return self.name

# Disease Model which translates to disease table in the DB
class Disease(models.Model):
    name = models.CharField(max_length=100)
    disease_symptoms = models.TextField()
    treatment_plan = models.TextField()
    crop = models.ForeignKey(Crop, related_name='crop', on_delete=models.SET_NULL, null=True)
    pesticide = models.ForeignKey(Pesticide, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg',
                              blank=True, upload_to='images/')

    def __str__(self):
        return self.name

class Post(models.Model):
    
    crop=models.ForeignKey(Crop,  on_delete=models.SET_NULL, null=True)
    description=models.TextField()
    image = models.ImageField(default='default.jpg',blank=True, upload_to='images/')

    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=True)
# Role Model which translates to role table in the DB
# class Role(models.Model):
#     name = models.CharField(max_length=100)

# class User(AbstractUser):
#     pass
# class User(models.Model):
   
#     name = models.CharField(max_length=100)
#     county = models.CharField(max_length=100)
#     mobile=models.IntegerField()
#     role= models.ForeignKey(Role,  on_delete=models.SET_NULL, null=True)
    

# Create your models here.

# Pest Model which translates to pest table in the DB
class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    # shop_name = models.ForeignKey(Shop, to_field="name", db_column="name",related_name='shop_name', on_delete=models.SET_NULL, null=True)
    pesticide = models.ForeignKey(Pesticide, on_delete=models.SET_NULL, null=True)
    # pesticide_image = models.ForeignKey(Pesticide, to_field="image", db_column="image",related_name='pesticide_image', on_delete=models.SET_NULL, null=True)
    # pesticide_name = models.ForeignKey(Pesticide, to_field="name", db_column="pesticide_name", related_name='pesticide_name', on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    def __str__(self):
        return self.name
