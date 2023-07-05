from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    # object = models.Manager() # by default this is set

    student = models.Manager()


