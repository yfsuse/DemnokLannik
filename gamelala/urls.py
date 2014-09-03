from django.conf.urls import patterns, include, url
from sdk.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index$', index),
    url(r'^dencrypt$', dencrypt),
    url(r'^druidreport', show_report),
    url(r'^result$', get_report_data),
    url(r'^autoreport', autoreport),
    # Examples:
    # url(r'^$', 'gamelala.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
