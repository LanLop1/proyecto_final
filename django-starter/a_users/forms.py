from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.forms import SignupForm
from django.db import transaction

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'displayname', 'info', 'nombre', 'apellido', 'phone', 'address']
        widgets = {
            'image': forms.FileInput(),
            'displayname': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info': forms.Textarea(attrs={'rows':3, 'placeholder': 'Add information'})
        }

class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']



class CustomSignupForm(SignupForm):
    nombre = forms.CharField(max_length=200, label='Nombre', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Nombre'
    }))
    apellido = forms.CharField(max_length=200, label='Apellido', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apellidos'
    }))
    phone = forms.CharField(max_length=200, label='Teléfono', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Teléfono'
    }))
    address = forms.CharField(max_length=200, label='Dirección', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Dirección'
    }))

    @transaction.atomic
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.refresh_from_db()
        profile, created = Profile.objects.get_or_create(user=user)
        profile.phone = self.cleaned_data.get('phone')
        profile.address = self.cleaned_data.get('address')
        profile.nombre = self.cleaned_data.get('nombre')
        profile.apellido = self.cleaned_data.get('apellido')
        profile.save()
        return user