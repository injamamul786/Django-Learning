from django.db import models

# Create your models here.
class User(models.Model):
    st_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tc_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)