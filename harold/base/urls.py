from django.conf.urls import patterns, url

from harold.base import api_views


urlpatterns = patterns(
    'harold.base.views',

    url(r'^/?$', 'index', name='base.index'),

    url(r'^submit/?$', 'submit_feedback', name='base.submit_feedback'),
    url(r'^feedback/(?P<feedback_id>\d+)/?$', 'view_feedback', name='base.view_feedback'),
    url(r'^thanks/?$', 'thanks', name='base.thanks'),

    url(r'^modify/(?P<feedback_id>\d+)/?$', 'modify_feedback', name='base.modify_feedback'),

    url(r'^api/v1/feedback/$',
        api_views.FeedbackAPI.as_view(), name='feedback-api'),
)
