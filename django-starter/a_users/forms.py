from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.hashers import make_password

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'displayname', 'info' ]
        widgets = {
            'image': forms.FileInput(),
            'displayname' : forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info' : forms.Textarea(attrs={'rows':3, 'placeholder': 'Add information'})
        }
        
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['email','contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        return make_password(contraseña)