from django.shortcuts import render
from mainapp.models import Company, DimsGlasses, Glasses, Face
from mainapp.forms import FaceForm

# Create your views here.
from django.conf.urls import *
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FaceForm

urlpatterns = patterns('mysite.views',
    (r'^upload_im/$', 'upload_im'),
    (r'^inp_coord/$', 'inp_coord'),
    (r'^glasses/$', 'glasses'),
)

def index(request):
	return render(request, 'mainapp/index.html')

def upload_face(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = FaceForm(request.POST, request.FILES)
		if form.is_valid():
			# file is saved
			form.save()

			return render_to_response("calibrate.html", {'form': form}, context)
	else:
		form = FaceForm()
	return render(request, 'mainapp/index.html')

def calibrate_face(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = RawFaceDataForm(request.POST)
		if form.is_valid():
			data = form.values()
			new_data = {}
			for item in data:
				split = item.split(',')
				new_data[int(split[0])] = int(split[1])
			new_data = sorted(new_data, key=new_data.get)
			new_form = FaceDataForm(new_data)
			if new_form.is_valid():
				new_form.save()
			return render_to_response("tryon.html", {})
	else:
		return render(request, 'mainapp/calibrate.html')

def tryon():
	pass

def get_face(request):
	""" May not be useful"""
	if request.method == 'POST':
		form = FaceForm(request.POST)
		if form.is_valid():
			my_method = form.save()
		else:
			form = FaceForm()

	return HttpResponse("Yay! Success!")

