from django.urls import path
from landing import views

urlpatterns=[
    path('', views.Home, name="Home")
]