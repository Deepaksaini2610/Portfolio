from django.db import models
from django.db.models.base import Model

# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to ='about/',blank = False)
    def __str__(self):
        return self.title
class slider(models.Model):
    slides = models.ImageField(upload_to = 'slid/',blank = False)
