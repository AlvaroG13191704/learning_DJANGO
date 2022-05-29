
from django.forms import EmailInput, ModelForm, TextInput

from django.forms import ModelForm
from personas.models import Domicilio

#Creamos una clase para generar el form
class DomicilioForm(ModelForm):
    class Meta:
        #Nuestro modelo de domicilio
        model = Domicilio
        fields = '__all__'
        #Para el espaciado de intenger
        Widgets = {
            'no_calle': TextInput(attrs={'type':'number'})
        }