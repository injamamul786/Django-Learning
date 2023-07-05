from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True # abstract is use so that table of this class not create, we only use data of this class but not create table.
                        # iss class ka table nhi banega ager ham abstract use ker lenge lekin iska data inherit kerwa sakte h dusare sub class me


class Student(CommonInfo):
    fees = models.IntegerField()
    date = None

class Teacher(CommonInfo):
    salary= models.IntegerField()

class Contractor(CommonInfo):
    date = models.DateTimeField() # this date overwrite base class date field
    payment = models.IntegerField()
