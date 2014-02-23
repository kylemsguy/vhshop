from django.conf.urls import patterns, url

from mainapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^calibrate$', views.calibrate_face, name='calibrate'),
    url(r'^try/$', views.tryon, name='tryon'),
)
