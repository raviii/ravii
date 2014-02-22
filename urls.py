from django.conf.urls import *
from gallery.settings import ROOT_URL
from django.views.generic import TemplateView
#urlpatterns = patterns('',
#    url(r'^%s' % ROOT_URL[1:], include('gallery.real_urls')),
#)

from gallery.views import StaticView

urlpatterns = patterns('home',(r'^$', TemplateView.as_view(template_name="index.html")))
