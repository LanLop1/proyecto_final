from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import ProductForm, ImageForm
from .models import Product
from a_home.models import Image

@require_http_methods(["GET", "POST"])
def create_product(request):
    product_form = ProductForm()
    image_form = ImageForm()

    if request.method == 'POST':
        if 'product_submit' in request.POST:
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product = product_form.save()
                return HttpResponse(f"<div id='product-{product.id}'>{product.name} creado exitosamente!</div>")
        elif 'image_submit' in request.POST:
            image_form = ImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                image = image_form.save()
                return HttpResponse(f'<option value="{image.id}">{image.file.name}</option>')
    
    return render(request, 'create_product.html', {
        'product_form': product_form,
        'image_form': image_form
    })

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})