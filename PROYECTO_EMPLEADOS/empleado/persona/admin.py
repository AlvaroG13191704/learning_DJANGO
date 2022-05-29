from django.contrib import admin
from persona.models import Habilidades

from persona.models import Empleado

# Register your models here.

admin.site.register(Habilidades)

#Here can work with admin tools
class EmpleadoAdmin(admin.ModelAdmin):
    #Table 
    list_display = (
        'first_name',
        'last_name',
        'job',
    )
    #Search
    search_fields = (
        'first_name',
    )
    #Filter
    list_filter = (
        'job',
    )

admin.site.register(Empleado,EmpleadoAdmin)