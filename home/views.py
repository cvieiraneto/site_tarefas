from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, World")

def home(request):
    return render(request, 'helloworld.html')

def helloworld(request):
    return render(request, 'helloworld.html')

def printar_nome(request, nome):
    return render(request, 'printarNome.html', {'nome': nome})