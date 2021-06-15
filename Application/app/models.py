"""
Definition of models.
"""

from django.db import models

class Pest(models.Model):
    name = models.CharField(max_length=100)
    pest_symptoms=models.TextField()
    treatment_plan=models.TextField()
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self._check_long_column_names

class Disease(models.Model):
    name = models.CharField(max_length=100)
    disease_symptoms=models.TextField()
    treatment_plan=models.TextField()
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
class Plant(models.Model):
    name = models.CharField(max_length=100)
    scientific_name=models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', blank=True, upload_to=user_directory_path)
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    disease=models.ForeignKey(Disease,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True) # date only when created, cant update this
  
    def __str__(self):
        return self.name

# Create your models here.
