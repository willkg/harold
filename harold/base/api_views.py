import rest_framework.views
import rest_framework.response


class FeedbackAPI(rest_framework.views.APIView):
    def post(self, request):
        raise Exception('Error is here!')
