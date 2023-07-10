from django.contrib import admin
from .models import Suma

class SumaAdmin(admin.ModelAdmin):
    readonly_fields=("precio", "porcentaje", "resultado", "created")

admin.site.register(Suma, SumaAdmin)
