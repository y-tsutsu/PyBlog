from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', "django.views.debug.default_urlconf"),   # 初期画面も出したい
    url(r'^entries/', include("entries.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
