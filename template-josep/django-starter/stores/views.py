from django.shortcuts import render, get_object_or_404
from .models import Store
from products.models import Product

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
    
    # Obtener todos los productos de la tienda
    products = Product.objects.filter(store=store)
    
    # Obtener las categorías únicas para los productos de esta tienda
    categories = Product.objects.filter(store=store).values_list('category', flat=True).distinct()
    
    context = {
        'store': store,
        'products': products,
        'categories': categories
    }
    
    return render(request, 'stores/shop.html', context)

def product_detail(request, product_id):
    # Obtén el producto o muestra una página 404 si no se encuentra
    product = get_object_or_404(Product, id=product_id)
    
    # Pasa el producto al template
    return render(request, 'stores/shop-single.html', {'product': product})
