from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=150)
    marks = models.IntegerField(null=True)
    pass_date = models.DateField()
    