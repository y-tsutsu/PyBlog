# coding: utf-8

from django.contrib import admin
from entries.models import Entry

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',              {'fields':['title']}),
        ('Detail information', {'fields':['pub_date', 'content'], 'classes':['collapse']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    date_hierarchy = 'pub_date'

admin.site.register(Entry, EntryAdmin)
