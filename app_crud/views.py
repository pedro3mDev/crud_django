from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def listar(request):
    return HttpResponse("Pagina de listar")
    #return render( request, 'index.html' )    
# end def

def cadastrar(request):
    return HttpResponse("Pagina de cadastro")
# end def

def editar(request):
    return HttpResponse("Pagina de Ediçao")
# end def

def eliminar(request):
    return HttpResponse("Pagina de Eliminaçao")
# end def