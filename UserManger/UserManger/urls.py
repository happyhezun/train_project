from django.conf.urls import patterns, include, url
from django.contrib import admin
import web01

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'UserManger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^web01/', include('web01.urls')),
)
