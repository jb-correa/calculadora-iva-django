from django.urls import path, include
from suma import views


urlpatterns=[
    path('sumar', views.sumar, name="Sumar")
]