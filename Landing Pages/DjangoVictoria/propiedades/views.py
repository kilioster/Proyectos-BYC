from django.shortcuts import render, redirect
from .models import Casa
# Create your views here.
def propiedades(request):
    casas = Casa.objects.all()
    return render(request, '../templates/propiedades.html', {'casas': casas})