from django.conf.urls.defaults import *
from django.conf import settings


#################
# INCLUDE VIEWS	#
#################

from brokenseal.admin import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/(.*)',	admin.site.root),
	url(r'^rosetta/',	include('rosetta.urls')),
	url(r'^robots.txt$', include('robots.urls')),
)
