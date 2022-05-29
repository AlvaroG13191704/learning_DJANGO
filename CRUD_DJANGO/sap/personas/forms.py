from django.forms import EmailInput, ModelForm


from django.forms import ModelForm
from personas.models import Persona
#Lo hacemos con una clase para que sea más personalizado

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__' # Indicamos que vamos a usar todos los modelos
        #Tipo de campo del form persona
        widgets = {
            'email': EmailInput(attrs={
                'type': 'email' #Importamos propiedades de HTML
            })
        }
