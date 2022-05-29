

from django import forms
from persona.models import Empleado
#Create a form
class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = '__all__'
        #Widgets---
        widgest = {
            'first_name': forms.TextInput( 
                attrs={
                    'placeholder':'Ingrese su nombre'
                }
            )
        }