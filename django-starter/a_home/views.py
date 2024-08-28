from django.shortcuts import render, get_object_or_404
from .models import Article
from products.models import Product
from django.shortcuts import render
from rest_framework import serializers
from django.db.models import Q

def home_view(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})



def search_view(request):
    query = request.GET.get('q')
    busquedas = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).order_by('-createdat')[:5]
    serializer = serializers(busquedas, many=True)
    return render(request, 'busqueda_resultados.html', {'resultados': serializer.data})


def article_detail_view(request, id):
        article = get_object_or_404(Article, id=id)
        return render(request, 'article_detail.html', {'article': article})

def search_object(request):
     search_text=request.POST.get('search')
     results = Product.objects.filter(name__icontains=search_text)
     context = {'results' : results}
     return render(request,'/partials/search-object.html')
     pass

