from django.conf.urls import patterns, include, url
from sdk.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^main$', parser),
    url(r'^req', send_req),
    url(r'^result$', show),
    # Examples:
    # url(r'^$', 'gamelala.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
