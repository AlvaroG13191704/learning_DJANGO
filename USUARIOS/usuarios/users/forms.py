from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs= {
                'placeholder':'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs= {
                'placeholder':'Repetir contraseña'
            }
        )
    )
    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    #Validaciones
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no son las mismas')
    def clean_passwords(self):
        password1 = self.cleaned_data['password1']
        if len(password1) < 5:
            self.add_error('password1','Contraseña muy corta')

class UserLoginForm(forms.Form):
    """Form definition for UserLogin."""
    username = forms.CharField(
        label='Username',
        required=True,
        widget= forms.TextInput(
            attrs= {
                'placeholder':'Ingrese su username'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget= forms.PasswordInput(
            attrs= {
                'placeholder':'Ingrese su contraseña'
            }
        )
    )

class UpdatePasswordForm(forms.Form):
    """Form definition for UpdatePassword."""
    password = forms.CharField(
        label='Contraseña:',
        required=True,
        widget= forms.PasswordInput(
            attrs= {
                'placeholder':'Ingrese su contraseña actual'
            }
        )
    )
    password_new = forms.CharField(
        label='Contraseña nueva:',
        required=True,
        widget= forms.PasswordInput(
            attrs= {
                'placeholder':'Ingrese su nueva contraseña'
            }
        )
    )
