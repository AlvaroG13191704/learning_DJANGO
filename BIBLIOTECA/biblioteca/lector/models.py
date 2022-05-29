
from django.db import models
from .managers import PrestamoManager
from libro.models import Libro
# Create your models here.
#Abstrac class
from autor.models import Persona
class Lector(Persona):
    class Meta:
        verbose_name = 'Lector'


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE,related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True,null=True)
    devuelto = models.BooleanField(default=False)
    #manager
    objects = PrestamoManager()
    #def PARA CUAndo se guarda un modelo
    def save(self,*args,**kwargs):
        print('GUARDANDO')
        self.libro.stok = self.libro.stok - 1
        self.libro.save()
        super(Prestamo,self).save(*args,**kwargs)

    def __str__(self):
        return self.libro.titulo