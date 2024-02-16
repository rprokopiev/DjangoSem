from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from datetime import datetime
from randomapp.models import HeadsTailsResult


logger = logging.getLogger(__name__)


def index(request): 
    logger.info('ranadomapp - index')
    http = '<h1>Welcome to RANDOMAPP</h1>'
    return HttpResponse(http) 


def heads_tails(request):
    result = choice(['HEADS', 'TAILS'])
    logger.info(f'{result}')
    time_now = datetime.now()
    game_result = HeadsTailsResult(result=result, time=time_now)
    game_result.save()
    logger.info(f'HeadsTails #{game_result.pk} Model created')
    return HttpResponse(f'<h1>{result} {time_now}</h1>')


def dice(request):
    result = randint(1, 6)
    logger.info(f'dice: {result}')
    return HttpResponse(f'<h1>{result}</h1>')


def random_int(request):
    result = randint(0, 100)
    logger.info(f'dice: {result}')
    return HttpResponse(f'<h1>{result}</h1>')
