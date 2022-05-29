from tabnanny import verbose
from django.db import models

# Create your models here.
class Departamento(models.Model):
    #Atributes
    name = models.CharField('Name',max_length=50)
    short_name = models.CharField('Short name', max_length=20)

    #The class meta you can get better presentation of your data in the admin section
    class Meta:
        #Modifie the title
        verbose_name = 'Department'
        #Ordering 
        ordering = ['-name']
        #prevents register the same register two times
        unique_together = ('name','short_name')
    def __str__(self):
        return self.name + "-" + self.short_name