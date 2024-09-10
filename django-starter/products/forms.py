from django import forms
from .models import Product
from a_home.models import Image
from stores.models import Store

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ProductForm(forms.ModelForm):
    image = forms.ModelChoiceField(
        queryset=Image.objects.all(),
        required=False,
        label="Imagen del producto",
        help_text="Seleccione una imagen para el producto (opcional)"
    )

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stockquantity', 'image', 'category']
        labels = {
            'name': 'Nombre del producto',
            'description': 'Descripción',
            'price': 'Precio',
            'stockquantity': 'Cantidad en stock',
            'category': 'Categoría',
        }
        help_texts = {
            'name': 'Ingrese el nombre del producto',
            'description': 'Proporcione una descripción detallada del producto',
            'price': 'Ingrese el precio del producto (debe ser mayor que cero)',
            'stockquantity': 'Ingrese la cantidad disponible en stock',
            'category': 'Seleccione la categoría que mejor describe su producto',
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProductForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.user:
            try:
                store = Store.objects.get(owner=self.user)
                cleaned_data['store'] = store
            except Store.DoesNotExist:
                raise forms.ValidationError("El usuario no tiene una tienda asociada.")
        return cleaned_data

    def save(self, commit=True):
        instance = super(ProductForm, self).save(commit=False)
        if self.user:
            instance.store = self.cleaned_data['store']
        if commit:
            instance.save()
        return instance