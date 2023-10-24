from django.db import models
from django.forms import ModelForm


class Suma (models.Model):
    precio=models.FloatField()
    porcentaje=models.FloatField()
    resultado=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name="Suma"
        verbose_name_plural="Sumas"
    def __str__(self):
        return "Suma del día "+self.created
    def __init__(self):
        ##iva=self.precio*self.porcentaje/100
        ##self.resultado=self.precio+iva
        return self.resultado

class SumaForm(ModelForm):
    class Meta:
        model=Suma
        fields=['precio', 'porcentaje']