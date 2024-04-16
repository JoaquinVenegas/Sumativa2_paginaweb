from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class Juegos (models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID de juego', null=False)
    nombre = models.CharField(max_length=50, verbose_name='Nombre de juego', null=False)
    precio = models.IntegerField(verbose_name='Precio de juego', null=False)
    cantidad = models.IntegerField(verbose_name='Cantidad de juego',null=False)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class Usuario (models.Model):
    id_user = models.AutoField(primary_key=True, verbose_name='ID de usuario', null=False)
    username = models.CharField(max_length=60, verbose_name='Nombre de usuario', null=False)
    password = models.CharField(max_length=12, verbose_name='Contraseña de usuario', null=False)
    correo = models.CharField(max_length=50, verbose_name='Correo de usuario', null=False)
    fecha_nac = models.DateField(verbose_name='Fecha de nacimiento', null=False)

    def __str__(self):
        return self.username
    
class Perfil (models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name='Usuario', primary_key=True)
    descripcion = models.CharField(max_length=150, verbose_name='Descripcion de perfil')

    def __str__(self):
        return self.descripcion
    
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=settings.ROLES)

    def __str__(self):
        return self.user.username + '-' +self.rol