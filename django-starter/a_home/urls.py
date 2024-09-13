from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome_view, name="pagina_home"),
]