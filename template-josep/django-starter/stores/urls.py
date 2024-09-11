from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('_<int:store_id>/', views.store_detail, name='store_detail'),
    path('_<int:store_id>/index/', views.store_index, name='store_index'),
    path('_<int:store_id>/about/', views.store_about, name='store_about'),
    path('_<int:store_id>/contact/', views.store_contact, name='store_contact'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

]
