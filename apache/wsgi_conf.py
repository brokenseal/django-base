import os, sys
import django.core.handlers.wsgi


os.environ['DJANGO_SETTINGS_MODULE']= 'example.settings'
application = django.core.handlers.wsgi.WSGIHandler()
