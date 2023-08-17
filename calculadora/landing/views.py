from django.shortcuts import render, redirect
from suma.models import Suma, SumaForm
from deduccion.models import Deduccion, DeduccionForm


def Home(request):

    def sumar(request):
        form=SumaForm()
        if request.method =='POST':
            form=SumaForm(data=request.POST)
        if form.is_valid():
            suma=form.save()     
            redirect("Suma")
        else:
            form=suma()
        return render(request, 'suma/suma.html', {"form": form})

    def deducir(request):
        form=DeduccionForm()
        if request.method =='POST':
            form=DeduccionForm(data=request.POST)
        if form.is_valid():
            Deduccion=form.save()     
            redirect("Deduccion")
        else:
            form=Deduccion()
        return render(request, 'deduccion/deduccion.html', {"form": form})

    return render(request, 'landing/home.html')