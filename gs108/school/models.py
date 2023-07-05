from django.db import models
from .managers import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    

class ProxyStudent(Student):
    student = CustomManager() 
    class Meta:
        proxy = True
        ordering = ['name']

