from django import forms
from .models import Product
from a_home.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-textarea block w-full mt-1'}),
            'file': forms.FileInput(attrs={'class': 'form-input block w-full mt-1'}),
        }

class ProductForm(forms.ModelForm):
    image = forms.ModelChoiceField(
        queryset=Image.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={
            'class': 'form-select block w-full mt-1 rounded border-gray-300 focus:border-indigo-500 focus:ring-indigo-500',
        })
    )

    class Meta:
        model = Product
        fields = ['store', 'name', 'description', 'price', 'stockquantity', 'image']
        widgets = {
            'store': forms.Select(attrs={
                'class': 'form-select block w-full mt-1 rounded border-gray-300 focus:border-indigo-500 focus:ring-indigo-500',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-input block w-full mt-1 rounded border-gray-300 focus:border-indigo-500 focus:ring-indigo-500',
                'placeholder': 'Nombre del producto',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea block w-full mt-1 rounded border-gray-300 focus:border-indigo-500 focus:ring-indigo-500',
                'rows': 4,
                'placeholder': 'Describe el producto...',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input block w-full mt-1 rounded border-gray-300 focus:border-indigo-500 focus:ring-indigo-500',
                'placeholder': 'Precio',
            }),
            'stockquantity': forms.NumberInput(attrs={
                'class': 'form-input block w-full mt-1 rounded border-gray-300 focus:border-indigo-500 focus:ring-indigo-500',
                'placeholder': 'Cantidad en stock',
            }),
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

