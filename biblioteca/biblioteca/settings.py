import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '81=czgs*!w@#miln65@qia^1mg!v@hnsp4er%rb5fgkd*xm%zt'
########## END SECRET CONFIGURATION


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
########## END SITE CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    # DJANGO REST FRAMEWORK
    'rest_framework',
    'corsheaders',
)

LOCAL_APPS = (
    'django_extensions',
    'mockups',
)

BASE_APPS = (
    'dewey',
    'author',
    'publisher',
    'book',
    'thesis',
    'brochure',
    'law',
    'magazine'
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + BASE_APPS

if DEBUG:
    INSTALLED_APPS  += LOCAL_APPS

########## END APP CONFIGURATION


########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES_DJANGO = (
    # Default Django milddleware:
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

MIDDLEWARE_CLASSES_THIRD_PARTY = (
    # framework corsheaders
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES_DJANGO + MIDDLEWARE_CLASSES_THIRD_PARTY
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'biblioteca.urls'
########## END URL CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'biblioteca.wsgi.application'
########## END WSGI CONFIGURATION
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'es'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Caracas'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL  = '/static/'
MEDIA_URL   = '/media/'

MEDIA_ROOT  = '/home2/formatco/www/django/media/'
STATIC_ROOT = '/home2/formatco/www/django/static/'

TEMPLATE_DIRS = (
    '/home2/formatco/www/django/templates/',
)

if DEBUG:
    STATIC_ROOT = 'static/'
    MEDIA_ROOT  = 'media/'
    TEMPLATE_DIRS = (
        '../web/django/templates/',
    )

########## END GENERAL CONFIGURATION


########## REST CONFIGURATION
REST_FRAMEWORK = {
    'PAGINATE_BY': 8,           # Default to 10
    'PAGINATE_BY_PARAM': 'size', # Allow client to override, using `?size=xxx`.
    'MAX_PAGINATE_BY': 30        # Maximum limit allowed when using `?size=xxx`.
}
########## END REST CONFIGURATION

########## CORS-HEADERS CONFIGURATION
#Everyone can connect
CORS_ORIGIN_ALLOW_ALL = True
#Add Permitted Clients
CORS_ORIGIN_WHITELIST = ()
########## END CORS-HEADERS CONFIGURATION
