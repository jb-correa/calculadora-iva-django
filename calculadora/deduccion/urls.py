from django.contrib import admin
from django.urls import path
from deduccion import views


urlpatterns = [
    path('',views.deduccion, name="Deduccion"),
    path('sumado', views.deducido, name="Deducido")
    
]