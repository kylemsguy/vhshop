from django.conf.urls import patterns, include, url

from django.contrib import admin
from mainapp import urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vhshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vhshop/', include(urls))
)
