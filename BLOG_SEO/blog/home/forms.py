from django import forms

#
from .models import Suscribers

#model
class SuscribersForms(forms.ModelForm):

    class Meta:
        model = Suscribers
        fields = {
            'email',
        }
        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Correo electronico...',
                }
            )
        }