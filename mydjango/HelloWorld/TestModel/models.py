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


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
