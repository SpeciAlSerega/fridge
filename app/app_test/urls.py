from django.contrib import admin
from django.urls import include, path

from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('add/', add, name='add'),
    path('prices/', prices, name='prices'),
    path('spares/', spares, name='spares'),



]
