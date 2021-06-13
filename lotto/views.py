from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
import logging

logger = logging.getLogger(__name__)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def view_1_0(request):
    1 / 0
    return HttpResponse('')


def view_1_0_try(request):
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception(view_1_0_try)
    return HttpResponse('view_1_0_try')
