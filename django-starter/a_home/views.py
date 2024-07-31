from django.shortcuts import render, get_object_or_404
from .models import Article
def home_view(request):
    return render(request, 'home.html')

def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Article.objects.filter(title__icontains=query) | Article.objects.filter(content__icontains=query) | Article.objects.filter(resumen__icontains=query)
    return render(request, 'search_results.html', {'results': results, 'query': query})


def article_detail_view(request, id):
        article = get_object_or_404(Article, id=id)
        return render(request, 'article_detail.html', {'article': article})