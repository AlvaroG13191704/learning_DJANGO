
from django.db import models
from django.db.models import Q,Count,Avg,Sum

class PrestamoManager(models.Manager):
    #calcualr el promedio de edades
    """
    El aggragate devuelve un dic y tiene funciones
    """
    def edadesProm(self):
        resultado = self.filter(
            libro__id = "2"
        ).aggregate(
            promedio = Avg('lector__edad'),
            suma_edad =Sum('lector__edad')
        )
        return resultado
    #
    def librosPrestados(self):
        resultado = self.annotate(
            num_prestados = Count('libro')
        )
        return resultado