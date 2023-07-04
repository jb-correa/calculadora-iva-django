from django.urls import path
from django.conf import settings
from suma import views

urlpatterns = [
    
    path('', views.suma, name="Suma"),
    
]