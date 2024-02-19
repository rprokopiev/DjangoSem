from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from datetime import datetime
from randomapp.models import HeadsTailsResult, Dice, RandomInt


logger = logging.getLogger(__name__)


def index(request): 
    logger.info('ranadomapp - index')
    http = '<h1>Welcome to RANDOMAPP</h1>'
    return render(request, 'randomapp/index.html', context={'hello': http})


def heads_tails(request):
    result = choice(['HEADS', 'TAILS'])
    logger.info(f'{result}')
    game_result = HeadsTailsResult(result=result, time=datetime.now())
    game_result.save()
    logger.info(f'HeadsTails #{game_result.pk} Model created')
    return render(request, 'randomapp/randomint.html', context={'result': f'{game_result.result}'})

def dice(request):
    result = randint(1, 6)
    logger.info(f'{result}')
    game_result = Dice(result=result, time=datetime.now())
    game_result.save()
    logger.info(f'Dice # {game_result.pk} model created')
    return render(request, 'randomapp/randomint.html', context={'result': f'{game_result.result}'})


def random_int(request):
    result = randint(0, 100)
    logger.info(f'Random Int: {result}')
    game_result = RandomInt(result=result, time=datetime.now())
    game_result.save()
    logger.info(f'Random Int # {game_result.pk} model created')
    return render(request, 'randomapp/randomint.html', context={'result': f'{game_result.result}'})

