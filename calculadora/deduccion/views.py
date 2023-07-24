from django.shortcuts import render
from .models import Deduccion

def deducir(request):
    d=Deduccion()
    return render(request, 'deduccion/deduccion.html', {"d", d})
