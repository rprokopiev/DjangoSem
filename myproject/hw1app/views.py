from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('INDEX page raised')
    context = {'text':"""My first site ---my first site---"""}
    return render(request, 'hw1app/index.html', context)


def main(request):
    logger.info('MAIN page raised')
    text="""
    <h1>My MAIN page</h1>
    <p><---My main page--></p>
    """
    return render(request, 'hw1app/main.html', context={'text': text})


def about(request):
    logger.info('ABOUT page raised')
    html="""
    <h1>Page about me</h1> 
    <p><---Page about me---></p>
    """
    return render(request, 'hw1app/about.html', context={'text':html})