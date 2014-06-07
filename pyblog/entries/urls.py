﻿# coding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from entries.models import Entry

urlpatterns = patterns('entries.views',
    url(r'^$',
        ListView.as_view(
            queryset = Entry.objects.order_by("-pub_date"),
            template_name = "entries/list.html")),
    url(r'^(?P<entry_id>\d+)/$', 'detail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
