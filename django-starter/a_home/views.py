from django.shortcuts import render, get_object_or_404
from .models import Article
from products.models import Product
from django.shortcuts import render
from rest_framework import serializers
from django.db.models import Q, Count
from stores.models import Store

def home_view(request):
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

    category_filter = request.GET.get('category')
    sort_option = request.GET.get('sort', 'name')  # Default sorting by 'name'

    if category_filter:
        stores = Store.objects.filter(products__category=category_filter).distinct()
    else:
        stores = Store.objects.all()

    # Sort stores based on the selected option
    if sort_option == 'name':
        stores = stores.order_by('name')
    elif sort_option == 'name_desc':
        stores = stores.order_by('-name')
    # Add more sorting options if needed

    # Get the count of stores per category based on having at least one product in that category
    category_counts = {
        code: Store.objects.filter(products__category=code).distinct().count()
        for code in category_dict.keys()
    }

    # Convert category counts to a list of tuples
    category_list = [(code, category_dict[code], category_counts[code]) for code in category_dict]

    return render(request, 'home.html', {
        'stores': stores,
        'category_list': category_list,
        'category_dict': category_dict,
        'sort_option': sort_option
    })


def welcome_view(request):
     return render(request, 'Pagina_Inicio/index.html')

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def empty_view(request):
     return render(request, 'includes/empty_div.html')

def search_view(request):
    query = request.GET.get('search')
    busquedas = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).order_by('-createdat')[:5]
    
    return render(request, 'busqueda_resultados.html', {'resultados': busquedas})


def article_detail_view(request, id):
        article = get_object_or_404(Article, id=id)
        return render(request, 'article_detail.html', {'article': article})

def search_object(request):
     search_text=request.POST.get('search')
     results = Product.objects.filter(name__icontains=search_text)
     context = {'results' : results}
     return render(request,'/partials/search-object.html')
     pass

