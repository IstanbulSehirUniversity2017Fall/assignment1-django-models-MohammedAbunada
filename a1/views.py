# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. This is a test.")

def GetBook(request,book_id):
    return HttpResponse("%s"%(Book.objects.get(pk=book_id)))

