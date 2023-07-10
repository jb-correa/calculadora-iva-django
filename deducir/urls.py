from django.urls import path
from django.conf import settings
from deducir import views

urlpatterns = [
    
    path('', views.deduccion, name="Deducir"),
    
]