"""
WSGI config for harold project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import logging
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "harold.settings")

import django
from django.core.handlers.wsgi import WSGIHandler
from django.conf import settings
from django.views import debug
from django.utils import six

from dj_static import Cling


class BetterDebugMixin(object):
    """Provides better debugging data

    Developing API endpoints and tired of wading through HTML for HTTP
    500 errors?

    Working on POST API debugging and not seeing the POST data show up in
    the error logs/emails?

    Then this mixin is for you!

    It:

    * adds a "postbody" section to the error logs/emails that has the first
      10,000 bytes of the raw post content

Handler mixin that overrides handle_uncaught_exception to provide better debug data

    """
    def handle_uncaught_exception(self, request, resolver, exc_info):
        if settings.DEBUG_PROPAGATE_EXCEPTIONS:
            raise

        logger = logging.getLogger('django.request')

        # This should be "bytes" here, though in Python 2, that's a
        # str type.
        postbody = getattr(request, 'body', '')
        try:
            # For string-ish data, we truncate and encode in utf-8.
            postbody = postbody[:10000].encode('utf-8')
        except UnicodeEncodeError:
            # For binary, we say, 'BINARY CONTENT'
            postbody = 'BINARY CONTENT'

        logger.error('Internal Server Error: %s', request.path,
            exc_info=exc_info,
            extra={
                'status_code': 500,
                'request': request,
                'postbody': postbody
            }
        )

        if settings.DEBUG:
            # request.is_ajax() == True will push this into doing text
            # instead of html which is waaaaaayyy more useful from an
            # API perspective. So if the Accept header is anything other
            # than html, we'll say it's an ajax request to return text.
            if 'html' not in request.META.get('HTTP_ACCEPT', 'text/html'):
                request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
            return debug.technical_500_response(request, *exc_info)

        # If Http500 handler is not installed, re-raise last exception
        if resolver.urlconf_module is None:
            six.reraise(*exc_info)
        # Return an HttpResponse that displays a friendly error message.
        callback, param_dict = resolver.resolve500()
        return callback(request, **param_dict)


class HaroldWSGIHandler(BetterDebugMixin, WSGIHandler):
    pass


def get_wsgi_application():
    django.setup()
    return HaroldWSGIHandler()


application = Cling(get_wsgi_application())
