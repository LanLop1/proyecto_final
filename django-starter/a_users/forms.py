from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'displayname', 'info', 'phone', 'address', 'nombre', 'apellido']
        widgets = {
            'image': forms.FileInput(),
            'displayname' : forms.TextInput(attrs={'placeholder': 'Nombre visible'}),
            'info' : forms.Textarea(attrs={'rows':3, 'placeholder': 'Añadir información'}),
            'phone' : forms.TextInput(attrs={'placeholder': 'Añadir telefono'}),
            'address' : forms.TextInput(attrs={'placeholder': 'Añadir dirección'}),
            'nombre' : forms.TextInput(attrs={'placeholder': 'Añadir nombre'}),
            'apellido' : forms.TextInput(attrs={'placeholder': 'Añadir apellidos'}),
        }
        
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']