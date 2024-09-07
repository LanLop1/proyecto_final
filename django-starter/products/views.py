from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import ProductForm, ImageForm
from .models import Product
from a_home.models import Image
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
@require_http_methods(["GET", "POST"])
def create_product(request):
    product_form = ProductForm(user=request.user)
    image_form = ImageForm()

    if request.method == 'POST':
        if 'product_submit' in request.POST:
            product_form = ProductForm(request.POST, request.FILES, user=request.user)
            if product_form.is_valid():
                product = product_form.save()
                return HttpResponse(f"<div id='product-{product.id}'>{product.name} creado exitosamente!</div>")
        elif 'image_submit' in request.POST:
            image_form = ImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                image = image_form.save(commit=False)
                image.user = request.user
                image.save()
                return HttpResponse(f'<option value="{image.id}">{image.file.name}</option>')
    
    return render(request, 'create_product.html', {
        'product_form': product_form,
        'image_form': image_form
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    html = render_to_string('product_detail.html', {'product': product})
    return HttpResponse(html)

def add_to_cart(request, product_id):
    # Aquí iría la lógica para añadir el producto al carrito
    # Por ahora, solo devolvemos un contador ficticio
    return HttpResponse("1")  # Devuelve el nuevo número de items en el carrito

def product_shop_view(request, id):
    product = get_object_or_404(Product, id=id)

    # Redirigir si la solicitud es HTMX
    if request.headers.get('HX-Request'):
        return HttpResponseRedirect(request.path) 

    return render(request, 'product_shop.html', {'product': product})