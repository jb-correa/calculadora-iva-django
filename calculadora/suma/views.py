from django.shortcuts import render, HttpResponse
from .models import Suma

def suma(request):
    suma=Suma()

    return render(request, '', {"suma", suma})

