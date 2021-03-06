from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm
from .models import CustomUser, Escribano
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('nombre', 'apellido', 'dni', 'email',)



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('nombre', 'apellido', 'dni', 'email',)



class EscribanoCreationForm(UserCreationForm):
    opciones = (('Buenos Aires', 'Buenos Aires'), ('Capital Federal', 'Capital Federal'),
        ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'),
        ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'),
        ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'),
        ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'),
        ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'),
        ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'),
        ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'),
        ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán'),
        )
    
    matrícula = forms.IntegerField()
    provincia = forms.ChoiceField(choices=opciones)
    ciudad = forms.CharField(max_length=50)
    calle = forms.CharField(max_length=50)
    altura = forms.IntegerField()
    piso = forms.IntegerField(required=False)
    número_de_puerta = forms.CharField(max_length=4, required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'nombre', 'apellido', 'dni', 'email', 'matrícula', 'provincia', 'ciudad',
            'calle', 'altura', 'piso', 'número_de_puerta',
            )
    
    def save(self):
        user = super(EscribanoCreationForm, self).save()
        user.is_escribano = True
        user.save()
        matricula = self.cleaned_data['matrícula']
        provincia = self.cleaned_data['provincia']
        ciudad = self.cleaned_data['ciudad']
        calle = self.cleaned_data['calle']
        altura = self.cleaned_data['altura']
        piso = self.cleaned_data['piso']
        numeroPuerta = self.cleaned_data['número_de_puerta']
        user = Escribano.objects.create(
            customuser_ptr=user, matricula = matricula, provincia = provincia,
            ciudad = ciudad, calle = calle, altura = altura, piso= piso,
            numeroPuerta = numeroPuerta
            )
        return user

class EscribanoEditForm(ModelForm):
    opciones = (('Buenos Aires', 'Buenos Aires'), ('Capital Federal', 'Capital Federal'),
    ('Catamarca', 'Catamarca'), ('Chaco', 'Chaco'), ('Chubut', 'Chubut'),
    ('Córdoba', 'Córdoba'), ('Corrientes', 'Corrientes'), ('Entre Ríos', 'Entre Ríos'),
    ('Formosa', 'Formosa'), ('Jujuy', 'Jujuy'), ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'), ('Mendoza', 'Mendoza'), ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquén'), ('Río Negro', 'Río Negro'), ('Salta', 'Salta'),
    ('San Juan', 'San Juan'), ('San Luis', 'San Luis'), ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'), ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego', 'Tierra del Fuego'), ('Tucumán', 'Tucumán'),
    )
    
    provincia = forms.ChoiceField(choices=opciones)
    ciudad = forms.CharField(max_length=50)
    calle = forms.CharField(max_length=50)
    piso = forms.IntegerField(required=False)

    class Meta:
        model = Escribano
        fields = ('provincia', 'ciudad', 'calle', 'altura', 'piso', 'numeroPuerta')