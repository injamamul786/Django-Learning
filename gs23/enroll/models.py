from django.db import models

# Create your models here.
class  Student(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=80)
    stupass = models.CharField(max_length=70)
    comment = models.CharField(max_length=50, default="Not available")

