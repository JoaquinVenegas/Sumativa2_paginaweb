from django import forms
from django.forms import ModelForm
from .models import Juegos, Usuario, Perfil

class JuegosForm(ModelForm):

    class Meta:
        model = Juegos
        fields = ['id', 'nombre', 'precio', 'cantidad', 'imagen']

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['id_user','username','password','correo','fecha_nac']

class PerfilForm(ModelForm):

    class Meta:
        model = Perfil
        fields = ['usuario', 'descripcion']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)