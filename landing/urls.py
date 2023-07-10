from django.urls import path
from django.conf import settings
from landing import views

urlpatterns = [
    
    path('', views.home, name="Home"),
    
]