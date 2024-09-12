from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from a_home.models import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from stores.models import Store
from products.models import Product
from stores.forms import StoreForm 
from django.template.loader import render_to_string
from django.shortcuts import  get_object_or_404
from django.http import HttpResponseRedirect

@login_required
@require_http_methods(["GET", "POST"])
def create_or_edit_store(request):
    try:
        store = Store.objects.get(owner=request.user)
        editing = True
    except Store.DoesNotExist:
        store = None
        editing = False

    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            if not editing:
                store.owner = request.user
            
            # Manejo de imágenes
            for field_name in ['imageStore', 'logoImage', 'bannerImage']:
                if field_name in request.FILES:
                    image_file = request.FILES[field_name]
                    image = Image.objects.create(
                        user=request.user,
                        file=image_file,
                        description=f"{field_name} for {store.name}"
                    )
                    setattr(store, field_name, image)
            
            store.save()
            action = "actualizada" if editing else "creada"
            messages.success(request, f"Tu tienda ha sido {action} exitosamente.")
            return redirect(reverse('stores:create_or_edit_store'))
    else:
        form = StoreForm(instance=store)
    
    context = {
        'form': form,
        'editing': editing,
    }
    return render(request, 'stores/create_or_edit_store.html', context)


def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    html = render_to_string('store_detail.html', {'store': store})
    return HttpResponse(html)

def store_shop_view(request, id):
    store = get_object_or_404(Store, id=id)

    # Redirigir si la solicitud es HTMX
    if request.headers.get('HX-Request'):
        return HttpResponseRedirect(request.path) 

    return render(request, 'store_shop.html', {'store': store})

def store_index(request, store_id):
    print("store_id", store_id)
    store = get_object_or_404(Store, id=store_id)

    products = Product.objects.filter(store=store).order_by('price')  # Ascendente (menor a mayor)

    # Obtener las categorías únicas para los productos de esta tienda
    categories = Product.objects.filter(store=store).values_list('category', flat=True).distinct()
    
    context = {
        'store': store,
        'products': products,
        'categories': categories,
    }
    
    return render(request, 'stores/index.html', context)

def store_about(request, store_id):
    store = get_object_or_404(Store, id=store_id)

    products = Product.objects.filter(store=store).order_by('price')  # Ascendente (menor a mayor)

    # Obtener las categorías únicas para los productos de esta tienda
    categories = Product.objects.filter(store=store).values_list('category', flat=True).distinct()
    
    context = {
        'store': store,
        'products': products,
        'categories': categories
    }
    
    return render(request, 'stores/about.html', context)

def store_contact(request, store_id):
    store = get_object_or_404(Store, id=store_id)

    products = Product.objects.filter(store=store).order_by('price')  # Ascendente (menor a mayor)

    # Obtener las categorías únicas para los productos de esta tienda
    categories = Product.objects.filter(store=store).values_list('category', flat=True).distinct()
    
    context = {
        'store': store,
        'products': products,
        'categories': categories
    }
    
    return render(request, 'stores/contact.html', context)


# Vista para listar todas las tiendas
def store_list(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/store_list.html', context)
    

# Vista para mostrar los detalles de una tienda específica
def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)

    sort_by = request.GET.get('sort', 'name')  # Por defecto ordenar por nombre
    # Obtener todos los productos de la tienda
    if sort_by == 'price_asc':
        products = Product.objects.filter(store=store).order_by('price')  # Ascendente (menor a mayor)
    elif sort_by == 'price_desc':
        products = Product.objects.filter(store=store).order_by('-price')  # Descendente (mayor a menor)
    else:
        products = Product.objects.filter(store=store).order_by('name')  # Por defecto alfabéticamente
    
    # Obtener las categorías únicas para los productos de esta tienda
    categories = Product.objects.filter(store=store).values_list('category', flat=True).distinct()
    
    context = {
        'store': store,
        'products': products,
        'categories': categories
    }
    
    return render(request, 'stores/shop.html', context)

def product_detail(request, product_id):
    # Diccionario de categorías
    category_dict = {
        'SIN': 'Sin categoría',
        'LIB': 'Libros',
        'TEC': 'Tecnología',
        'JAR': 'Jardinería',
        'ROP': 'Ropa',
        'HOG': 'Hogar',
        'ELE': 'Electrónicos',
        'DEP': 'Deportes',
        'JUG': 'Juguetes',
        'ORD': 'Ordenadores y Accesorios',
        'MOV': 'Móviles y Accesorios',
        'COS': 'Cosmética y Belleza',
        'SAL': 'Salud y Cuidado Personal',
        'ALM': 'Alimentos y Bebidas',
        'BEB': 'Bebés y Niños',
        'AUT': 'Automóviles y Motocicletas',
        'MUS': 'Música e Instrumentos Musicales',
        'VID': 'Videojuegos',
        'PEL': 'Películas y Series',
        'MAS': 'Mascotas y Animales',
        'OFI': 'Oficina y Papelería',
        'HERR': 'Herramientas y Mejoras del Hogar',
        'CAL': 'Calzado',
        'REC': 'Recreación al Aire Libre',
        'JOY': 'Joyas y Relojes',
        'VIA': 'Viajes y Equipaje',
        'ART': 'Arte y Manualidades',
        'JUE': 'Juegos de Mesa y Puzzles'
    }

    # Obtén el producto o muestra una página 404 si no se encuentra
    product = get_object_or_404(Product, id=product_id)

    # Obtén la categoría del producto actual
    product_category_code = product.category

    # Reemplaza las siglas de categoría con la frase completa si es necesario para mostrar
    product.category = category_dict.get(product_category_code, 'Categoría desconocida')

    # Obtén productos relacionados (de la misma categoría) de todas las tiendas excepto el actual
    related_products = Product.objects.filter(category=product_category_code).exclude(id=product.id)

    # Pasa el producto y los productos relacionados al template
    context = {
        'product': product,
        'related_products': related_products
    }

    return render(request, 'stores/shop-single.html', context)