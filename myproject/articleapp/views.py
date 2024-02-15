from django.shortcuts import render
from django.http import HttpResponse 
import logging


logger = logging.getLogger(__name__)


def index(request): 
    logger.info('articleapp - index')
    http = '<h1>Welcome to ARTICLEAPP</h1>'
    return HttpResponse(http) 


def about(request): 
    logger.info('articleapp - about us')
    return HttpResponse("About us")
