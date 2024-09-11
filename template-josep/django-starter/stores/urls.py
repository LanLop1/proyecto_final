from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('_<int:store_id>/', views.store_detail, name='store_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
