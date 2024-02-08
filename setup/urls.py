from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from crud.views import index
from crud.views import listar
 
urlpatterns = [
    path('', index),
    path('listar/', listar),
]
