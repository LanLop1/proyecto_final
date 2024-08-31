"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_users.views import profile_view
from a_home.views import *
from a_home.views import search_view, article_detail_view, search_object, product_detail, search_view
from products.views import  add_to_cart, product_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name="home"),
    path('buscar/', search_view, name='search_view'),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),
    path('article/<int:id>/', article_detail_view, name='article_detail'),
    path('', include('chat_support.urls'), name='chat_support'),
    path('', include('notifications.urls'), name='notifications'),
    path('orders/', include('orders.urls'), name='orders'),
    path('', include('products.urls'), name='productSergio/django-starters'),
    path('stores/', include('stores.urls', namespace='stores')),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/modal/', product_detail, name='product_detail'),
]


htmx_urlpatterns= [
    path('search/', search_view, name='search'),
    path('searchobject/', search_object, name='search-object')

]
urlpatterns += htmx_urlpatterns
# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
