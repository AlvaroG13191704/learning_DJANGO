from django import forms

#
from .models import Contact, Suscribers

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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('__all__')