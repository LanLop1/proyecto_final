from django.shortcuts import render, get_object_or_404
from .models import Store
from products.models import Product

def store_index(request, store_id):
    store = get_object_or_404(Store, id=store_id)

    products = Product.objects.filter(store=store).order_by('price')  # Ascendente (menor a mayor)

    # Obtener las categorías únicas para los productos de esta tienda
    categories = Product.objects.filter(store=store).values_list('category', flat=True).distinct()
    
    context = {
        'store': store,
        'products': products,
        'categories': categories
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
    
    # Reemplaza las siglas de categoría con la frase completa
    product.category = category_dict.get(product.category, 'Categoría desconocida')
    
    # Pasa el producto al template
    return render(request, 'stores/shop-single.html', {'product': product})
