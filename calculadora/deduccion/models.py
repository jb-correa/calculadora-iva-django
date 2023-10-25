from django.db import models
from django.forms import ModelForm

class Deduccion(models.Model):
    precio=models.FloatField()
    porcentaje=models.FloatField()
    resultado=models.FloatField(null=True)
    fecha=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name="Deduccion"
        verbose_name_plural = "Deducciones"
        ordering=['fecha']
    def __str__(self) :
        return f'Deduccion del día {self.fecha.day, self.fecha.month, self.fecha.year}'
    
class DeduccionForm(ModelForm):
    class Meta:
        model=Deduccion
        fields=['precio', 'porcentaje']
