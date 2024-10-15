from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def propiedades(request):
    return render(request, 'propiedades.html', {})