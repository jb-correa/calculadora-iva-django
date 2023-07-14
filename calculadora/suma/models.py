from django.db import models
from django.forms import ModelForm


class Suma (models.Model):
    precio=models.FloatField()
    porcentaje=models.FloatField()
    resultado=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)

class EjercicioForm(ModelForm):
    class Meta:
        model=Suma
        fields=['precio', 'porcentaje']