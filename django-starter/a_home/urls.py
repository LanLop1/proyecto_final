from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name="pagina_home"),
    path('search/', search_view, name='search'),
    path('article/<int:id>/', article_detail_view, name='article_detail'),
]