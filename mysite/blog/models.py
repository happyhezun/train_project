from django.db import models
from django.contrib import admin

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=16)
    body = models.TextField()
    timestamp = models.DateTimeField()

    #def __unicode__(self):
        #return self.title
    
    class Meta:
        ordering = ('-timestamp',)