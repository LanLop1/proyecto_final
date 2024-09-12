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
from a_home.views import product_detail, search_view, empty_view
from products.views import  product_detail, product_shop_view, product_detail_with_related, product_list
from stores.views import  store_detail, store_shop_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', home_view, name="home"),
    path('', welcome_view, name="pagina_home"),
    path('buscar/', search_view, name='search_view'),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),
    path('article/<int:id>/', article_detail_view, name='article_detail'),
    path('', include('chat_support.urls'), name='chat_support'),
    path('', include('notifications.urls'), name='notifications'),
    path('orders/', include('orders.urls'), name='orders'),
    path('', include('products.urls'), name='productSergio/django-starters'),
    path('stores/', include('stores.urls')),
    path('store/<int:id>/', store_shop_view, name='store_shop_view'),
    path('detail/<int:store_id>/', store_detail, name='store_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/<int:id>/', product_shop_view, name='product_shop_view'),
    path('product/<int:id>/detail/', product_detail_with_related, name='product_detail_with_related'),
    path('product-list/', product_list, name='product_list'),
    
]


htmx_urlpatterns= [
    path('search/', search_view, name='search'),
    path('searchobject/', search_object, name='search-object'),
    path('empty/', empty_view, name='empty'),
]
urlpatterns += htmx_urlpatterns


# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
