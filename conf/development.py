### development settings

DEBUG= True
SECRET_KEY= 'm(1-yb!eg34f*ve_w$z$#*8e=_fd@qte8yjjpgk+5andsoonPk'

STATIC_URL= 'http://dev_media.example.com/'
MEDIA_URL= STATIC_URL

# db
DATABASE_ENGINE = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_NAME= ''
DATABASE_USER = ''
DATABASE_PASSWORD = ''

MIDDLEWARE_CLASSES+= (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INSTALLED_APPS+= (
    'debug_toolbar',
)

# debug toolbar settings
DEBUG_TOOLBAR_PANELS = (
	'debug_toolbar.panels.version.VersionDebugPanel',
	'debug_toolbar.panels.timer.TimerDebugPanel',
	'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
	'debug_toolbar.panels.headers.HeaderDebugPanel',
	'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
	'debug_toolbar.panels.template.TemplateDebugPanel',
	'debug_toolbar.panels.sql.SQLDebugPanel',
	'debug_toolbar.panels.signals.SignalDebugPanel',
	'debug_toolbar.panels.logger.LoggingPanel',
)

def show_toolbar_callback(request):
	return True

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
	'SHOW_TOOLBAR_CALLBACK': show_toolbar_callback,
	'HIDE_DJANGO_SQL': False,
}
