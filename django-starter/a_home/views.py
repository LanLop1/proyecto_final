from django.shortcuts import render, get_object_or_404
from .models import Article
from products.models import Product
from django.shortcuts import render
from rest_framework import serializers
from django.db.models import Q
from stores.models import Store

def home_view(request):
    stores = Store.objects.all()
    return render(request, 'home.html', {'stores': stores})
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

