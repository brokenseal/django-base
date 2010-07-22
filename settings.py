import os

PROJECT_ROOT= os.path.abspath(os.path.dirname(__file__))
WEB_SITE_NAME= 'example'

STATIC_ROOT= os.path.join(PROJECT_ROOT, "media")
STATIC_URL= 'http://media.example.com/'

MEDIA_ROOT= STATIC_ROOT
MEDIA_URL= STATIC_URL

DEBUG = False
TEMPLATE_DEBUG= DEBUG

PREPEND_WWW= False

DATE_FORMAT= 'j N Y'			# 4 Feb. 2007
DATETIME_FORMAT= 'j N Y, H:i'	# 4 Feb. 2007, 16:00
TIME_FORMAT= 'H:i'				# 16:00
MONTH_DAY_FORMAT= 'j F'			# 6 January

URL_VALIDATOR_USER_AGENT= 'Django'

ADMINS = (
	('Callegari Davide', 'admin@example.com'),
)

SITE_ID = 1

TIME_ZONE = 'Europe/Rome'

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.debug',
	'django.core.context_processors.request',
)

LANGUAGE_CODE = 'en'
DEFAULT_CHARSET= 'utf-8'
SESSION_COOKIE_AGE= 21600
SESSION_EXPIRE_AT_BROWSER_CLOSE= True

CACHE_MAX_ENTRIES= 400
CACHE_CULL_PERCENTAGE= 3

ADMIN_MEDIA_PREFIX = '%sadmin_media/' % MEDIA_URL

SESSION_COOKIE_NAME= '%s_session_id' % WEB_SITE_NAME

MANAGERS = ADMINS
USE_I18N= True

SECRET_KEY= 'm(1-yb!eg34f*ve_w$z$#*8e=_fd@qte8yjjpgk+5gzofxf0@k'

ROOT_URLCONF= '%s.urls' % WEB_SITE_NAME

TEMPLATE_DIRS= (
	os.path.join(PROJECT_ROOT, 'templates'),
)

MIDDLEWARE_CLASSES = (
	'django.middleware.gzip.GZipMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.csrf.middleware.CsrfMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.doc.XViewMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'localeurl.middleware.LocaleURLMiddleware',
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'localeurl',
	'rosetta',
	'robots',
	'google_analytics',
	'south',
)

_ = lambda s:s

LANGUAGES = (
	(u'it', _(u'Italian')),
	(u'en', _(u'English')),
)

GOOGLE_ANALYTICS_MODEL = True

from conf import *
