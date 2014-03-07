from mainapp.models import Company, DimsGlasses, Glasses, Face
from mainapp.forms import FaceForm, FaceDataForm

# Create your views here.
from django.conf.urls import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from .forms import FaceForm
from vhshop.settings import STATIC_URL, MEDIA_URL, MEDIA_ROOT

from mainapp.models import Company, DimsGlasses, Glasses, Face

import io

urlpatterns = patterns('mysite.views',
    (r'^upload_im/$', 'upload_im'),
    (r'^inp_coord/$', 'inp_coord'),
    (r'^glasses/$', 'glasses'),
)

APP_ROOT = "/home/kylemsguy/vhshop-server"

# overlay('face.jpg', 'glasses.png', 225, [(140, 185), (188, 185)], 50, 100).save('new.jpg')
from PIL import Image
from math import floor

def overlay(face: str, glasses: str, dim_width: int,
        coords_eyes: list, h_offset: int, v_offset: int):
        original_face = Image.open(face)
        original_glasses = Image.open(glasses)

        scale = dim_width / original_glasses.size[0]

        new_dims = floor(original_glasses.size[0] * scale), \
                                floor(original_glasses.size[1] * scale)

        new_glasses = original_glasses.resize(new_dims,
                Image.ANTIALIAS)

        mid_coords_eyes = floor((coords_eyes[0][0] + coords_eyes[1][0]) / 2),\
                                                floor((coords_eyes[1][0] + \
                                                       coords_eyes[1][1]) / 2)

        # implement rotation if have time

        original_face.paste(new_glasses, (h_offset,
                                          v_offset), new_glasses)

        return original_face

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
			return render(request, 'mainapp/calibrate.html', {'face': form.instance, 'image': form.instance.image.url})
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
	facefile = APP_ROOT + face.image.url
	glassesfile = APP_ROOT + glasses.picture.url
	print(facefile, glassesfile)
	myoverlay = overlay(facefile, glassesfile, 225, [
		(face.left_side_x, face.left_side_y),
		(face.right_side_x, face.right_side_y)], 50, 100)
	tempname = MEDIA_ROOT + "temp.jpg"
	myoverlay.save(tempname)

	company_list = Company.objects.all().order_by('CompName')
	glasses_list = Glasses.objects.all().order_by('likes')
	thedict = {'image': MEDIA_URL + "temp.jpg", 'company_list': company_list, \
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

# overlay('face.jpg', 'glasses.png', 225, [(140, 185), (188, 185)], 50, 100).save('new.jpg')
from PIL import Image
from math import floor

def overlay(face: str, glasses: str, dim_width: int,
            coords_eyes: list, h_offset: int, v_offset: int):
	original_face = Image.open(face)
	original_glasses = Image.open(glasses)

	scale = dim_width / original_glasses.size[0]

	new_dims = floor(original_glasses.size[0] * scale), \
				floor(original_glasses.size[1] * scale)

	new_glasses = original_glasses.resize(new_dims, 
		Image.ANTIALIAS)

	mid_coords_eyes = floor((coords_eyes[0][0] + coords_eyes[1][0]) / 2),\
						floor((coords_eyes[1][0] + \
                                                       coords_eyes[1][1]) / 2)

	# implement rotation if have time

	original_face.paste(new_glasses, (h_offset,
                                          v_offset), new_glasses)

	return original_face
