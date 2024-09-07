from django import forms
from .models import Store, QRCode
from a_home.models import Image, Template
from a_users.models import Profile
from django.contrib.auth.decorators import login_required


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['template', 'name', 'description', 'logourl', 'bannerurl']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
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