from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.http import HttpResponse
from .forms import UsuarioForm, PerfilForm, JuegosForm, LoginForm
from .models import Juegos, Usuario, Perfil, UserProfile
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

#@login_required
def juegos(request):

    producto = Juegos.objects.all()
    data= {
        'producto':producto
    }
    return render(request, 'juegos.html', data)

@login_required
def carrito(request):
    return render(request, 'carrito.html')

@login_required
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            request.session['perfil']=profile.rol
            login (request,user)
            return redirect('home')
        else:
            context = {'fallo al iniciar sesion'}

    return render(request, 'registration/login.html', context)

def registro(request):
    if request.method == 'POST':
        registro_form = UsuarioForm(request.POST)
        if registro_form.is_valid():
            registro_form.save()
            messages.success(request, "¡Registro exitoso!")
            return redirect('nombre_de_la_url')
        else:
            for field, errors in registro_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        registro_form = UsuarioForm()

    return render(request, 'registration/registro.html', {'form': registro_form})

def modificar(request):
    return render(request, 'registration/modificar.html')

def recuperar(request):
    return render(request, 'registration/recuperar.html')

def exit(request):
    logout(request)
    return redirect('index')


