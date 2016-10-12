from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
# from app01 import views

urlpatterns = patterns('',

    url(r'^index/', views.Model),
    url(r'^model/', views.ModelMut),

)
