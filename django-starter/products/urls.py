from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('upload-image', views.upload_image, name='upload_image'),
    # path('list/', views.product_list, name='product_list'),
]