from django.db import models

# Create your models here.

class Book(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=30)
    PDF = models.FileField(upload_to='book/pdf')
    Cover = models.ImageField(upload_to='book/cover',null=True,blank=True)
    