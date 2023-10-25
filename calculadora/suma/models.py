from typing import Any
from django.db import models
from django.forms import ModelForm


class Suma(models.Model):
    precio=models.FloatField()
    porcentaje=models.FloatField()
    resultado=models.FloatField(null=True)
    fecha=models.DateField(auto_now_add=True)
    def __str__(self):
        return f'Suma del día {self.fecha.day, self.fecha.month, self.fecha.year}'
    class Meta:
        verbose_name="comida"
        verbose_name_plural="comidas"
        ordering=['fecha']
        


class SumaForm(ModelForm):
    class Meta:
        model=Suma
        fields=['precio', 'porcentaje']