from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^index/', views.index),
    (r'^getdata/', views.menu),
    (r'^auth/$', views.Auth),
    (r'^getRegion/$', views.menu),

)
