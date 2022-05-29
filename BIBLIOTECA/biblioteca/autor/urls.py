from django.urls import path
from .views import listaAutores

urlpatterns = [
    path('lista/',listaAutores, name="lista_autores"),
]