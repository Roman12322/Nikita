from django.db import models

class User(models.Model):
    Login = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)

class Messaging(models.Model):
    First_Prime_Numbers = models.IntegerField()
    List = models.CharField(max_length=1000, null=True)
    Username_Id = models.IntegerField(max_length=1000, null=True)
