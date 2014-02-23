from django.shortcuts import render
from mainapp.models import Company, DimsGlasses, Glasses, Face
from mainapp.forms import FaceForm


# Create your views here.
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FaceForm

urlpatterns = patterns('mysite.views',
    (r'^upload_im/$', 'upload_im'),
    (r'^inp_coord/$', 'inp_coord'),
    (r'^glasses/', 'glasses'),
)

def index(request):
	return render(request, 'index.html')

def upload_face(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = FaceForm(request.POST, request.FILES)
		if form.is_valid():
			# file is saved
			form.save()

		return render_to_response(calibrate.html, {'form': form}, context)
	else:
        form = FaceForm()
    return 
    


def get_face(request):
    if request.method == 'POST':
        form = FaceForm(request.POST)
        if form.is_valid():
            my_method = form.save()
        else:
            form = FaceForm()

    return HttpResponse("Yay! Success!")
