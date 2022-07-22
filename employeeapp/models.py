from django.db import models

# Create your models here.

class Employee(models.Model):

    emp_id = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
    password = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True,blank=True)
    address = models.CharField(max_length=10, null=True,blank=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)
    text = models.CharField(max_length=1000, null=True, blank=True)
    binary = models.BinaryField(max_length=1000, null=True, blank=True)

