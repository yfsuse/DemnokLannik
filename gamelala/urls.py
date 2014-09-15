from django.conf.urls import patterns, include, url
from sdk.views import *
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views',
    url(r'/css/(?P<path>.*)$', 'static.serve',
        {'document_root':settings.STATIC_ROOT+'css/'}),
    url(r'/js/(?P<path>.*)$', 'static.serve',
        {'document_root':settings.STATIC_ROOT+'js/'}),
    url(r'/image/(?P<path>.*)$', 'static.serve',
        {'document_root':settings.STATIC_ROOT+'image/'}),
    url(r'^index$', index),
    url(r'^dencrypt$', dencrypt),
    url(r'^druidreport', show_report),
    url(r'^result$', get_report_data),
    url(r'^login', login),
    url(r'^autoreport', autoreport),
    # Examples:
    # url(r'^$', 'gamelala.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
