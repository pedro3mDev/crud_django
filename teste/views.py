from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def ver(request):
    return render(request, "teste/teste.html")  
# end def
