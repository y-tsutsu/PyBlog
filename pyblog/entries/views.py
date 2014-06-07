# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

def detail(request, entry_id):
    return HttpResponse("You're looking at the results of entry {0}.".format(entry_id))
