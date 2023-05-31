from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    email = models.EmailField()
    phone = models.CharField(max_length=10)

class EmployDetail(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=30)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    place = models.CharField(max_length=50)
    salary =models.IntegerField()