from django.db import models

class Suma (models.Model):
    precio=models.FloatField()
    porcentaje=models.FloatField()
    resultado=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)