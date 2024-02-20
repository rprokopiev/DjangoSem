from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse 
import logging
from .models import Author, Article, Comment


logger = logging.getLogger(__name__)


def index(request): 
    logger.info('articleapp - index')
    http = 'Welcome to ARTICLEAPP'
    return render(request, 'articleapp/index.html', context={'content': http})


def about(request): 
    logger.info('articleapp - about us')
    return render(request, 'articleapp/about.html', context={'content': 'about page'})


def articles_per_author(request, author_id):
    logger.info('articleapp - articles_per_author')
    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author)
    return render(request, 'articleapp/author_articles.html', {'author': author, 'articles': articles})


def article_view(request, article_id):
    logger.info('articleapp - articles_view')
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article_id=article.pk).order_by('id')
    article.views_count += 1
    article.save()
    return render(request, 'articleapp/article_view.html', {'article': article, 'comments': comments})
