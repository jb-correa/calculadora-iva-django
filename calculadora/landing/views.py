from django.shortcuts import render, redirect
from suma.models import Suma, SumaForm


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

    return render(request, 'landing/home.html')