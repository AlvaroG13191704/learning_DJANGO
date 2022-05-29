from django.db import models

# Create your models here.
"""
Primero se crean las clase que no tienen relacion
LLave foranea es un concepto de base de datos
    --> Relación entre dos tablas, se define dentro de la clase que se relaciona
"""
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio: {self.id}: {self.calle} {self.no_calle} {self.pais}'

#Esto creara una tabla en postgres
class Persona(models.Model):
    #Atributos estaticos, fuera de todo metodo
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    #Si se elimina un registro de la tabla de domicilio entonces, hacemos que se coloque null y concedemos el permiso que que ponga null
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return f'Persona: {self.id}: {self.nombre} {self.apellido} {self.email}'

