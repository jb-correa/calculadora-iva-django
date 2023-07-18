from django.contrib import admin
from .models import Suma

class SumaAdmin(admin.ModelAdmin):
    readonly_fields=("created")

admin.site.register(Suma, SumaAdmin)
