from django.conf.urls import patterns, include, url
from django.contrib import admin
from web01 import views

urlpatterns = patterns('',
    # Examples:
#     url(r'^index$', views.index),
    url(r'^$', views.show_user_list),
    url(r'^search_form$', views.search_from),    
    url(r'^search$', views.search),
    url(r'^addUser_form$', views.addUser_form),
    url(r'^addUser', views.AddUser),
    url(r'^list_sort/(.+)', views.list_sort),
    url(r'^test/(.+)', views.test),
        

)
