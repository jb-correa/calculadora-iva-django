from django.shortcuts import render
from .models import Deduccion

def deducir(request):
    d=Deduccion()
    list=d.from_db.__get__(all)
    list.sort()
    d=list[-1]
    return render(request, 'deduccion/deduccion.html', {"d", d})
