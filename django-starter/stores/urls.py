from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('create/', views.create_store, name='create_store'),
    path('list/', views.store_list, name='store_list'),
]