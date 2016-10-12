#coding:utf-8
from django.db import models

# Create your models here.
class FirstModel(models.Model):
    UserName = models.CharField(max_length=10)


class SecondModel(models.Model):
    Nid = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20, default='hanxin')
    Address = models.CharField(max_length=20, default='alex')
    Gender = models.BooleanField()
    Age = models.IntegerField(default=1)
#     CaiPiao = models.CommaSeparatedIntegerField()
    Data = models.DateField(auto_now_add=True)
    DateTime = models.DateTimeField(auto_now=True,default="2011-11-11")
    
    
    
class ThirdModel(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class ColorDic(models.Model):
    ColorName = models.CharField(max_length=20)
    
    def __unicode__(self):
#         字符顯示
        return self.ColorName
    
    
    
class Person(models.Model):
    Name = models.CharField(max_length=20)
    Gender = models.BooleanField(default=False)
    Color = models.ForeignKey(ColorDic)
    
    
    
class AuthorList(models.Model):
    Name = models.CharField(max_length=20)
    

class Book(models.Model):
    BookName = models.CharField(max_length=20)
    Author = models.ManyToManyField(AuthorList)
    