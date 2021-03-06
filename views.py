# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
import datetime
from django.template.loader import get_template
from django.template import Context

from django.shortcuts import render_to_response

def hello(request):
  return HttpResponse("Hello, World!")

def current_datetime(request):
  now = datetime.datetime.now()
  return render_to_response('current_datetime.html',{'current_date': now, 'name': "vasya"})

def hour_ahead(request,offset):
  try:
    offset = int(offset)
  except:
    raise Http404
  dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
  #assert False
  html = "<html><body>It is now %s.</body></html>" % dt
  return HttpResponse(html)
