# coding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, CreateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from entries.models import Entry
from entries.forms import HTML5Form

urlpatterns = patterns('entries.views',
    url(r'^$',
        ListView.as_view(
            queryset = Entry.objects.order_by('-pub_date'),
            template_name = 'entries/list.html')),
    url(r'^create/$',
        CreateView.as_view(
            model = Entry,
            success_url = '/entries/',
            template_name = 'entries/create.html',
            form_class = HTML5Form)),
    url(r'^(?P<entry_id>\d+)/$', 'detail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)

urlpatterns += staticfiles_urlpatterns()
