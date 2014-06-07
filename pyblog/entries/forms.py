# coding: utf-8

from django import forms
from django.forms import ModelForm
from entries.models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry   

class HTML5Form(EntryForm):
    def __init__(self, *args, **kwargs):
        super(HTML5Form, self).__init__(*args, **kwargs)
 
        for _, field in self.fields.items():
            if field.widget.is_required:
                field.widget.attrs['required title'] = "aaaaaa"
