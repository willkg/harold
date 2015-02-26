from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # harold urls
    url(r'', include('harold.base.urls')),

    # admin urls
    url(r'^admin/', include(admin.site.urls)),

    # django-browserid urls
    url(r'', include('django_browserid.urls')),
)
