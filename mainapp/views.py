from mainapp.models import Company, DimsGlasses, Glasses, Face
from mainapp.forms import FaceForm, FaceDataForm

# Create your views here.
from django.conf.urls import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from .forms import FaceForm
from vhshop.settings import STATIC_URL, MEDIA_ROOT
from standalone_scripts import image_overlay

from mainapp.models import Company, DimsGlasses, Glasses, Face

import io

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
			return render_to_response("calibrate.html", {'form': newform}, context)
	else:
		form = FaceForm()
	return render(request, 'mainapp/index.html')

def calibrate_face(request):
	if request.method == 'POST':
		form = FaceForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			newform = FaceDataForm(instance=form.instance)
			return render(request, 'mainapp/calibrate.html', {'face': form.instance, 'image': STATIC_URL + form.instance.image.url})
		else:
                        form = FaceDataForm(request.POST, request.FILES)
                        return HttpResponse("Form is not valid")
def parseinttuple(instr):
	a = instr.split(",")
	return int(a[0]), int(a[1])
def tryon(request):
	face = Face.objects.get(pk=request.GET['id'])
	if 'set1' in request.GET:
		(face.left_side_x, face.left_side_y) = \
			parseinttuple(request.GET['set1'])
		(face.right_side_x, face.right_side_y) = \
			parseinttuple(request.GET['set2'])
		face.left_corner_x, face_left_corner_y = \
			parseinttuple(request.GET['set3'])
		face.right_corner_x, face.right_corner_y = \
			parseinttuple(request.GET['set4'])
		face.save()
	glasses = Glasses.objects.all()[0]
	print(face.image, glasses.picture)
	facefile = MEDIA_ROOT + face.image.url
	glassesfile = MEDIA_ROOT + glasses.picture.url
	print(facefile, glassesfile)
	myoverlay = image_overlay.overlay(facefile, glassesfile, 225, [
		(face.left_side_x, face.left_side_y),
		(face.right_side_x, face.right_side_y)], 50, 100)
	tempname = MEDIA_ROOT + "temp.jpg"
	myoverlay.save(tempname)

	company_list = Company.objects.all().order_by('CompName')
	glasses_list = Glasses.objects.all().order_by('likes')
	thedict = {'image':STATIC_URL + "temp.jpg", 'company_list': company_list, \
		'glasses_list': glasses_list}

	return render_to_response("mainapp/tryon.html", thedict)

def get_face(request):
	""" May not be useful"""
	if request.method == 'POST':
		form = FaceForm(request.POST)
		if form.is_valid():
			my_method = form.save()
		else:
			form = FaceForm()

	return HttpResponse("Yay! Success!")

