from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.forms import SignupForm

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
        model = User
        fields = ['email']

class CustomSignupForm(SignupForm):
      nombre = forms.CharField(max_length=200, label='nombre', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Nombre'
    }))
      apellido = forms.CharField(max_length=200, label='apellido', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apellido'
    }))
      phone = forms.CharField(max_length=200, label='Phone', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Teléfono'
    }))
      address = forms.CharField(max_length=200, label='Address', required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Dirección'
    }))
      displayname = forms.CharField(max_length=20, label='Display Name', required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Usuario'
    }))
      
      def save(self, request):
            user = super(CustomSignupForm, self).save(request)
            user.profile.phone = self.cleaned_data.get('phone')
            user.profile.address = self.cleaned_data.get('address')
            user.profile.displayname = self.cleaned_data.get('displayname')
            user.profile.nombre = self.cleaned_data.get('nombre')
            user.profile.apellido = self.cleaned_data.get('apellido')
            user.profile.save()
            return user