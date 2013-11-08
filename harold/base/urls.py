from django.conf.urls import patterns, url

urlpatterns = patterns(
    'harold.base.views',

    url(r'^/?$', 'index', name='base.index'),

)
