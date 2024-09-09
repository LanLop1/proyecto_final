from django.urls import path
from . import views

app_name = 'stores'

urlpatterns = [
    path('create/', views.create_or_edit_store, name='create_or_edit_store'),
]