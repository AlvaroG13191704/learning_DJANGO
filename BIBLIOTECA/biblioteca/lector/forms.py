from django import forms
from .models import Prestamo
from libro.models import Libro
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro',
        )
#form con seleccion multiples 
class PrestamoMultipleForm(forms.ModelForm):
    libros = forms.ModelMultipleChoiceField(
        #podemos usar Libro.objects.all() o filtros
        queryset=None,
        required=True,
        widget = forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )
    #Para inicializar el forms
    def __init__(self, *args, **kwargs):
        super(PrestamoMultipleForm, self).__init__(*args, **kwargs)
        self.fields['libros'].queryset=Libro.objects.all()
