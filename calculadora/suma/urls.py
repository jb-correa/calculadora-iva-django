from django.contrib import admin
from django.urls import path
from suma import views


urlpatterns = [
    path('',views.suma, name="Suma"),
    path('sumado', views.sumado, name="Sumado")
    
]