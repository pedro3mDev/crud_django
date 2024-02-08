from django.shortcuts import render

def index(request):
    return render(request, "crud/index.html")  

def listar(request):
    return render(request, "crud/listar.html")

