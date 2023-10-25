from django.shortcuts import render,redirect
from .models import Deduccion, DeduccionForm


def deduccion(request):
    form=DeduccionForm()
    if request.method =='POST':
        form=DeduccionForm(data=request.POST)
        if form.is_valid():
            deduccion=form.save(commit=False)
            deduccion.resultado=deduccion.precio-(deduccion.precio*deduccion.porcentaje/100)
            deduccion.save()      
            return render(request, 'deduccion/deducido.html', {'deduccion': deduccion})
    else:
         form=DeduccionForm()
    return render(request, 'deduccion/deduccion.html', {"form": form})


def deducido (request):
    deducciones=Deduccion.objects.all()
    deduccion=deducciones[0]
    return render(request,'deduccion/deducido.html',{'deduccion': deduccion})