from django.urls import path
from . import views

urlpatterns= [
    path ('Juegos/', views.lista_juegos, name='lista_juegos'),
    path ('Juegos/<id>', views.vista_juegos, name='vista_juegos'),
]