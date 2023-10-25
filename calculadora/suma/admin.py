from django.contrib import admin
from .models import Suma

class SumaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'precio', 'porcentaje', 'resultado')
    list_per_page = 25
    readonly_fields=("fecha", "resultado")
admin.site.register(Suma, SumaAdmin)