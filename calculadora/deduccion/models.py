from typing import Any
from django.db import models
from django.forms import ModelForm

class Deduccion(models.Model):
    precio=models.FloatField()
    porcentaje=models.FloatField()
    resultado=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="Deducciones"
        verbose_name_plural="Deducciones"
    def __str__(self):
        return "Deducción del día "+self.created
    def __init__(self):
        iva=self.precio*self.porcentaje/100
        self.resultado=self.precio-iva

class DeduccionForm(ModelForm):
    class Meta:
        model=Deduccion
        fields=['precio', 'porcentaje']