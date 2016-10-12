from django.conf.urls import patterns, include, url
from django.contrib import admin
# from app01 import views

urlpatterns = patterns('',

#     url(r'^administrator/', include(admin.site.urls)),
    url(r'^admin/', include('app01.urls')),

)
'''
urlpatterns = patterns('app01.views',

    url(r'^views1/', 'index'),
)
urlpatterns += patterns('app02.views',

    url(r'^views2/', 'index'),
)
'''