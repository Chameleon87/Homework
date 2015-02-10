from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'members.views.MemberRegistration'),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^register/$', 'members.views.MemberRegistration'),
    url(r'^admin/', include(admin.site.urls)),
)
