from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import ProductForm, ImageForm
from .models import Product
from a_home.models import Image
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stores.models import Store


def create_product(request):
    try:
        store = Store.objects.get(owner=request.user)
    except Store.DoesNotExist:
        messages.error(request, "Debes crear una tienda antes de añadir productos.")
        return redirect('create_store')  # Asume que tienes una URL para crear tiendas

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.store = store  # Asocia el producto con la tienda del usuario
            
            # Handle image upload
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image = Image.objects.create(
                    user=request.user,
                    file=image_file,
                    description=f"Image for product: {product.name}"
                )
                product.image = image
            
            product.save()
            messages.success(request, f"{product.name} creado exitosamente!")
            return HttpResponse(status=204)
        else:
            for field, errors in product_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en {field}: {error}")
            return HttpResponse(status=400)
    else:
        product_form = ProductForm()
        products = Product.objects.filter(store=store)

    return render(request, 'create_product.html', {
        'product_form': product_form,
        'products': products,
    })
def product_detail_with_related(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'product_detail_with_related.html', context)

from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
@require_http_methods(["POST"])
def upload_image(request):
    image_form = ImageForm(request.POST, request.FILES)
    if image_form.is_valid():
        image = image_form.save(commit=False)
        image.user = request.user
        image.save()
        messages.success(request, f"Imagen '{image.file.name}' subida exitosamente.")
    else:
        for field, errors in image_form.errors.items():
            for error in errors:
                messages.error(request, f"Error al subir imagen - {field}: {error}")
    
    return HttpResponseRedirect(reverse('create_product'))



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    html = render_to_string('product_detail.html', {'product': product})
    return HttpResponse(html)

@login_required
def product_list(request):
    try:
        store = Store.objects.get(owner=request.user)
        products = Product.objects.filter(store=store)
        print("products", products)
    except Store.DoesNotExist:
        products = []
    return render(request, 'product_list_partial.html', {'products': products})

def product_shop_view(request, id):
    product = get_object_or_404(Product, id=id)

    # Redirigir si la solicitud es HTMX
    if request.headers.get('HX-Request'):
        return HttpResponseRedirect(request.path) 

    return render(request, 'product_shop.html', {'product': product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, store__owner=request.user)
    product.delete()
    return HttpResponse("", status=200)