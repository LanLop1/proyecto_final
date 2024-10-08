from django.urls import path
from stores.views import store_about,store_contact,store_shop_view,store_detail,store_index, product_detail_screen, create_or_edit_store

app_name = 'stores'

urlpatterns = [
    path('create/', create_or_edit_store, name='create_or_edit_store'),
    path('<int:store_id>/', store_detail, name='store_detail'),
    path('<int:store_id>/index/', store_index, name='store_index'),
    path('<int:store_id>/about/', store_about, name='store_about'),
    path('<int:store_id>/contact/', store_contact, name='store_contact'),
    path('product/<int:product_id>/', product_detail_screen, name='product_detail_screen'),
]