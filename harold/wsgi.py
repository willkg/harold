"""
WSGI config for harold project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "harold.settings.base")

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.wsgi import get_wsgi_application

from dj_static import Cling


if not settings.DEBUG:
    if settings.SECRET_KEY == 'r1ckylives':
        raise ImproperlyConfigured('DEBUG=False, so you must set SECRET_KEY')


application = Cling(get_wsgi_application())
