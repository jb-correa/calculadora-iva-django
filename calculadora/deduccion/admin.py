from django.contrib import admin
from .models import Deduccion

class DeduccionAdmin(admin.ModelAdmin):
    readonly_fields=("created")

admin.site.register(Deduccion,DeduccionAdmin)
