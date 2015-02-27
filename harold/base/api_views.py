from functools import wraps
import logging
import sys

from django.conf import settings
from django.views import debug

import rest_framework.request
import rest_framework.response
import rest_framework.views


def handle_api_uncaught_exception(request, exc_info):
    logger = logging.getLogger('django.request')

    # This kicks off the email that gets sent.
    logger.error('Internal Server Error: %s', request.path,
                 exc_info=exc_info,
                 extra={
                     'status_code': 500,
                     'request': request,
                     # Cut body off at 10000 bytes so logging isn't
                     # totally crazy.
                     'postbody': request.body[:10000]
                 }
             )

    if settings.DEBUG:
        # request.is_ajax() == True will push this into returning text
        # which is wayyyyy more useful from an API perspective than
        # HTML is. So we're going to turn that on even though this
        # may not be an ajax request.
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        return debug.technical_500_response(request, *exc_info)

    # Return an HttpResponse that displays a friendly error message.
    def view_500(request):
        pass

    return rest_framework.response.Response(
        status=500,
        data={
            'server-error': 'Server has kicked up an error. Sorry!'
        }
    )


def api_uncaught_exception_handler(fun):
    @wraps(fun)
    def _api_uncaught_exception_handler(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except:
            # We need to figure out which param was the request. It could
            # be the first (if we're wrapping a function) or the second
            # (if we're wrapping a method).
            #
            # FIXME: This is goofy.
            if isinstance(args[0], rest_framework.request.Request):
                request = args[0]
            else:
                request = args[1]
            return handle_api_uncaught_exception(request, sys.exc_info())
    return _api_uncaught_exception_handler


class FeedbackAPI(rest_framework.views.APIView):
    @api_uncaught_exception_handler
    def post(self, request):
        raise Exception('Error is here!')
