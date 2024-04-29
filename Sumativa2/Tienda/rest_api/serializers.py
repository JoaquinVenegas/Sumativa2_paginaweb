from rest_framework import serializers
from core.models import Juegos, Usuario

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Juegos
        fields= ['id', 'nombre', 'precio', 'cantidad', 'imagen']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= ['id_user', 'username', 'password', 'correo', 'fecha_nac']