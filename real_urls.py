from django.conf.urls import *
from django.contrib import admin

urlpatterns = patterns('',
#    url(r'^admin/(.*)', admin.site.root),
    url(r'^', include('gallery.items.urls')),
)
