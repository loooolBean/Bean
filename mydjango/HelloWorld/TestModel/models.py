from django.db import models

# Create your models here.
# class demo2(models.Model):
#     name = models.CharField(max_length=20)
#     id = models.CharField(max_length=20, primary_key=True)
# class Test(models.Model):
#     name = models.CharField(max_length=20)
class demo(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
