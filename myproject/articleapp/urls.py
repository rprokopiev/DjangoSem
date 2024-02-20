from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('author_articles/<int:author_id>', views.articles_per_author, name='articles_per_author'),
    path('article_view/<int:article_id>', views.article_view, name='article_view'),
]