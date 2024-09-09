from django import forms
from .models import Store, QRCode
from a_home.models import Image, Template
from a_users.models import Profile
from django.contrib.auth.decorators import login_required


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['template', 'name', 'description', 'horario' ,'dirección', 'imageStore']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'template': 'Template',
            'name': 'Nombre',
            'description': 'Descripción',
            'horario': 'Horario',
            'dirección': 'Dirección',
            'imageStore': 'Imagen del local'
        }


class QRCodeForm(forms.ModelForm):
    class Meta:
        model = QRCode
        fields = ['store', 'image']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }