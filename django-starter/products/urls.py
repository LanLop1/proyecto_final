from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]