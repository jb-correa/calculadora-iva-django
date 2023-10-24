from django.shortcuts import render, redirect
from suma.models import Suma, SumaForm
from deduccion.models import Deduccion, DeduccionForm


def Home(request):

    return render(request, 'home.html')