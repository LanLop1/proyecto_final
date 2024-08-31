from django import forms
from .models import Product
from a_home.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ProductForm(forms.ModelForm):
    image = forms.ModelChoiceField(queryset=Image.objects.all(), required=False)

    class Meta:
        model = Product
        fields = ['store', 'name', 'description', 'price', 'stockquantity', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return price

def clean_stockquantity(self):
        quantity = self.cleaned_data['stockquantity']
        if quantity < 0:
            raise forms.ValidationError("La cantidad en stock no puede ser negativa.")
        return quantity

