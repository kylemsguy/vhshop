from django.shortcuts import render

# Create your views here.
from django.conf.urls.defaults import *

urlpatterns = patterns('mysite.views',
    (r'^upload_im/$', 'upload_im'),
    (r'^inp_coord/$', 'inp_coord'),
    (r'^glasses/$, 'glasses')
)
