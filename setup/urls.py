from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from teste.views import ver
#from app_crud.views import listar
#from app_crud.views import editar
#from app_crud.views import eliminar
#from app_crud.views import cadastrar
 
urlpatterns = [
#    path('listar/', listar),
    path('', ver),
#    path('cadastrar/', cadastrar),
#    path('editar/', editar),
#    path('eliminar/', eliminar),
]
