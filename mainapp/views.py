from django.shortcuts import render
from mainapp.models import Company, DimsGlasses, Glasses, Face
from mainapp.forms import FaceForm, FaceDataForm

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
	ctx = {}
	if request.method == 'GET':
		form1 = FaceForm(request.GET)
		ctx['form1'] = form1
		return render(request, 'mainapp/index.html', ctx)

	if request.method == 'POST':
		form = FaceDataForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'mainapp/calibrate.html')

		else:
			form = FaceDataForm()
			ctx['form'] = form
			return render(request, 'mainapp/index.html', ctx)

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
	if request.method == 'POST':
		form = FaceDataForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpresponseRedirect('/')

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

