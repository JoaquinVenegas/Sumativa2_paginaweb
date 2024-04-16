from django.urls import path
from .views import index, carrito, juegos, home, login, registro, modificar, recuperar

urlpatterns = [
    path('', index, name='index'),
    path('index/juegos/', juegos, name='juegos'),
    path('index/carrito/', carrito, name='carrito'),
    path('index/home/', home, name='home'),
    path('accounts/login', login, name= 'login'),
    path('accounts/registro', registro, name= 'registro'),
    path('accounts/modificar', modificar, name='modificar'),
    path('accounts/recuperar', recuperar, name='recuperar'),
]