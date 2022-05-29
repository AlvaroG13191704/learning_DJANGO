
from tabnanny import verbose
from django.db import models
from departamento.models import Departamento
# Create your models here.
    #habilities
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)
    class meta:
        verbose_name = 'Hability'
    def __str__(self) -> str:
        return str(self.id) +'-'+ self.habilidad

class Empleado(models.Model):        
    #types
    JOB_CHOICES = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro'),
    )
    #Att
    first_name = models.CharField('Name' , max_length=60)
    last_name = models.CharField('Last name' , max_length=60)
    job = models.CharField('Job',max_length= 1,choices=JOB_CHOICES)
    #The foreing key
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado', blank = True, null=True)
    #A relations many to many
    habilidades = models.ManyToManyField(Habilidades)
    def __str__(self) -> str:
        return str(self.id) +'-'+self.first_name +'-'+ self.last_name