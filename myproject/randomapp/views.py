from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging


logger = logging.getLogger(__name__)


def index(request): 
    logger.info('ranadomapp - index')
    http = '<h1>Welcome to RANDOMAPP</h1>'
    return HttpResponse(http) 


def heads_tails(request):
    if randint(0, 1):
        logger.info('heads and tails: HEADS')
        return HttpResponse('<h1>HEADS</h1>')
    else: 
        logger.info('heads and tails: TAILS')
        return HttpResponse('<h1>TAILS</h1>')


def dice(request):
    result = randint(1, 6)
    logger.info(f'dice: {result}')
    return HttpResponse(f'<h1>{result}</h1>')


def random_int(request):
    result = randint(0, 100)
    logger.info(f'dice: {result}')
    return HttpResponse(f'<h1>{result}</h1>')
