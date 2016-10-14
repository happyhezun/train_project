#coding:utf-8
from django.db import models

# Create your models here.


class User(models.Model):
    UserName = models.CharField(max_length=50)
    PassWord = models.CharField(max_length=200)
    Gender = models.BooleanField(default="男")
    Age = models.IntegerField()
    Data = models.DateField(auto_now_add=True)
    DateTime = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.UserName

