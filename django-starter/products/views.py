from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import ProductForm, ImageForm
from .models import Product
from a_home.models import Image
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

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
@require_http_methods(["POST"])
def upload_image(request):
    image_form = ImageForm(request.POST, request.FILES)
    if image_form.is_valid():
        image = image_form.save()
        # Return some data or a success message
        return HttpResponse(f'<option value="{image.id}">{image.file.name}</option>')
    return HttpResponse("Error en la subida de la imagen", status=400)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    html = render_to_string('product_detail.html', {'product': product})
    return HttpResponse(html)

def add_to_cart(request, product_id):
    # Aquí iría la lógica para añadir el producto al carrito
    # Por ahora, solo devolvemos un contador ficticio
    return HttpResponse("1")  # Devuelve el nuevo número de items en el carrito

