from django.shortcuts import render
from mainapp.models import Company, DimsGlasses, Glasses, Face
from mainapp.forms import FaceForm


# Create your views here.
from django.conf.urls.defaults import *

urlpatterns = patterns('mysite.views',
    (r'^upload_im/$', 'upload_im'),
    (r'^inp_coord/$', 'inp_coord'),
    (r'^glasses/', 'glasses'),
)

def get_face(request):
    if request.method == 'POST':
        form = FaceForm(request.POST)
        if form.is_valid():
            my_method = form.save()
        else:
            form = FaceForm()
