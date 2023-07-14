from django.shortcuts import redirect, render
from .models import Suma, SumaForm

def sumar(request):
    
    return render(request, 'suma/suma.html')