from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    #Managers para autor
    """
    Los managers practicamente lo que hacen es poder crear funciones que hagan consultar 
    a nuestra base de datos, estas funciones pueden ser personalizadas y usadas en las views,
    es muy util para poder poder consultar de manera dinamica en base a nuestras funciones creadas
    """
    #Funcones
    #Traer todos los autores
    def listarAutores(self):
        return self.all()
    #Filtrar autores
    def buscar_autor(self,kword):
        resultado = self.filter(nombre__icontains=kword)
        return resultado
    #Filtrar con un or -- Esta usa una herramienta de django para poder usar el OR
    def buscar_autor2(self,kword):
        resultado = self.filter(Q(nombre__icontains=kword) | Q(apellidos__icontains=kword))
        return resultado
    #Filtrar y excluir algo
    def buscar_autor3(self,kword):
        resultado = self.filter(nombre__icontains=kword).exclude(edad=19)
        return resultado
    #Filter mayor igual y, para "y" usamos nomas una coma
    def buscar_autor_edad(self):
        resultado = self.filter(edad__gt=18)
        return resultado