from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day12_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^index/', views.index),
    (r'^getprovince/', views.GetProvince),
    (r'^getcity/', views.GetCity),
    (r'^getcounty/', views.GetCounty),
    
)
