from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('headstails/', views.heads_tails, name='Heads and Tails'),
    path('dice/', views.dice, name='Dice'),
    path('randomint/', views.random_int, name='Random Int'),
]