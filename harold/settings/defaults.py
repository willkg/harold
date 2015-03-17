# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from harold.settings_utils import config, NO_VALUE

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Instance settings that are required to be set either from
# environment or a settings module.
SECRET_KEY = config('SECRET_KEY', type_='str')
# FIXME: This should be a list of strings
BROWSERID_AUDIENCES = [
    config(
        'BROWSERID_AUDIENCES', default='http://127.0.0.1:8000', type_='str')
]

# FIXME: This should be a list of strings
ADMINS = config('ADMINS', default=None, type_='str')
if ADMINS is not None:
    admins_parts = '@'.split(admins)
    ADMINS = [(admins_parts[0], admins)]
else:
    ADMINS = []

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///harold.db')
}

# SECURITY WARNING: don't run with debug turned on in production!
TEMPLATE_DEBUG = config('DEBUG', default=True, type_='bool')
DEBUG = config('DEBUG', default=True, type_='bool')

ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_browserid.auth.BrowserIDBackend',
)

LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/'
LOGOUT_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_browserid',

    'harold.base',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'harold.urls'

WSGI_APPLICATION = 'harold.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
