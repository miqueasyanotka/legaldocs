from django import forms
from django.forms import ModelForm
from .models import Documento
from .validators import validate_file_extension


class DocumentoForm(ModelForm):
    título = forms.CharField(max_length=50)
    descripción = forms.CharField(max_length=300, required=False)
    número_de_páginas = forms.IntegerField()
    archivo = forms.FileField(required=False, validators=[validate_file_extension])

    class Meta:
        model = Documento
        fields = ('titulo', 'descripcion', 'paginas', 'archivo')