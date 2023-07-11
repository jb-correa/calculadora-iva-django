from django.db import models

class Suma(models.Model):
    precio=models.FloatField( )
    porcentaje=models.FloatField()
    resultado= models.FloatField()
    created= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='suma'
        verbose_name_plural='sumas'
    def __str__(self):
        return 'Suma del día '+self.created