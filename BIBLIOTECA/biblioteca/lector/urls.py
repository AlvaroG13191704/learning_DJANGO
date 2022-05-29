from django.urls import path
from .views import registar_prestamo, addPrestamo, addPrestamo_multiple

urlpatterns = [
    path('prestamo/registrar/',addPrestamo, name="registrar_prestamo"),
    path('prestamo/registrar/multiple/',addPrestamo_multiple, name="registrar_prestamo_m"),
]