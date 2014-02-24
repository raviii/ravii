import os.path
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/srv/django/gallery/book.db'

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True

#Get the absolute path of the settings.py file's directory
PWD = os.path.dirname(os.path.realpath(__file__ )) 

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or 
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    #Add Templates to the absolute directory
    os.path.join(PWD, "templates") 
)


SECRET_KEY = 'iy@w6)#gctex-omuue%k!t2=42)_*o__%5xqd#pc^q2iq5b8c*'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',  
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'gallery.items',
    'django.contrib.staticfiles',
)

STATICFILES_DIRS = (os.path.join(PWD, "static"),)
STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.FileSystemFinder',
   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Root URL prefix - e.g. '/gallery/' would be for non-top-level domain
ROOT_URL = '/'
LOGIN_URL = ROOT_URL + 'login/'
MEDIA_URL = ROOT_URL + 'media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = PWD + '/static'
STATIC_URL= '/static/'
STATIC_ROOT= '/static'
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'gallery.context_processors.root_url_processor',
)
ROOT_URLCONF = 'gallery.urls'
