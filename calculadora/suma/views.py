from django.shortcuts import render, redirect
from .models import Suma, SumaForm
from django.contrib import messages

def suma(request):
    form=SumaForm()
    if request.method =='POST':
        form=SumaForm(data=request.POST)
        if form.is_valid():
            suma=form.save(commit=False)
            suma.resultado=suma.precio+(suma.precio*suma.porcentaje/100)
            suma.save()      
            return render(request, 'suma/sumado.html', {'suma': suma})
    else:
         form=SumaForm()
    return render(request, 'suma/suma.html', {"form": form})

def sumado(request):
    sumas=suma.objects.all()
    suma=sumas[0]
    return render(request, 'suma/sumado.html', {'suma', suma})