from django.urls import path
from deduccion import views


urlpatterns=[
    path('deduccion', views.deducir, name="Deducir"),
]