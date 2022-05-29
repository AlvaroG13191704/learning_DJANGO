from django.contrib import admin

from personas.models import Persona
from personas.models import Domicilio

# Register your models here.
#Registrando modelo de personas
admin.site.register(Persona)
admin.site.register(Domicilio)