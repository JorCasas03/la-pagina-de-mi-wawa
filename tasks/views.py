from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Bicycle  # Importa el modelo Bicycle
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from .models import Profile
from django.contrib import messages, auth
from sweetify import warning, success
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.db.models import Q
from .forms import CarouselImageForm
from .models import CarouselImage






def remove_from_cart(request, bicycle_id):
    # Obtener el producto del carrito
    bicycle = get_object_or_404(Bicycle, id=bicycle_id)
    
    # Eliminar el producto del carrito
    bicycle.en_el_carrito = False
    bicycle.save()
    success(request, 'Producto eliminado correctamente')

    # Redirigir de vuelta a la página del carrito
    return HttpResponseRedirect(reverse('cart'))

# Define la función cart para el carrito de compras
def cart(request):
    bicycles = Bicycle.objects.filter(en_el_carrito=True)
    total = sum(bicycle.price for bicycle in bicycles)
    return render(request, 'cart.html', {'bicycles': bicycles, 'total': total})

def add_to_cart(request, bicycle_id):
    # Obtener la bicicleta con el ID proporcionado
    bicycle = get_object_or_404(Bicycle, id=bicycle_id)
    
    # Marcar la bicicleta como "en el carrito"
    bicycle.en_el_carrito = True
    bicycle.save()
    success(request, 'Producto agregado correctamente')

    # Redirigir de vuelta a la página de tareas
    return redirect('tasks')

# Resto de tus funciones de vista existentes...

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            success(request, 'Usuario creado correctamente')
            return redirect('home')
        else:
            warning(request, 'Contraseña muy corta y/o no coincidentes')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

def tasks(request):
    bicycles = Bicycle.objects.all()
    return render(request, 'tasks.html', {'bicycles': bicycles})

def signout(request):
    logout(request)
    success(request, 'Sesión cerrada correctamente')
    return redirect('home')

def signin(request):
    if request.method == 'POST':
        datos_usuario = AuthenticationForm(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            usuario = authenticate(
                username = datos_usuario.cleaned_data['username'],
                password = datos_usuario.cleaned_data['password']
            )
            if usuario is not None:
                login(request, usuario)
                success(request, f'Bienvenido {usuario.username}')
                return redirect('teamowawa')

        warning(request, 'Usuario y contraseña invalidos')
        contexto = {
        'form': datos_usuario
        }
        return render(request,"signin.html",contexto)
    else:
        context ={
            'form': AuthenticationForm()
        }
        return render(request,"signin.html",context)
        
def perfil(request):
    # Obtener el perfil del usuario actualmente autenticado
    profile = Profile.objects.get(user=request.user)
    return render(request, 'perfil.html', {'profile': profile})

@login_required
def edit_perfil(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user.first_name = form.cleaned_data['first_name']
            profile.user.last_name = form.cleaned_data['last_name']
            profile.user.save()
            profile.save()
            success(request, 'Cambios realizados correctamente')
            return redirect('perfil')
    else:
        form = EditProfileForm(instance=profile)
    
    return render(request, 'editPerfil.html', {'form': form})

def teamowawa(request):
    carousel_images = CarouselImage.objects.all()  # Obtener todas las imágenes del carrusel
    return render(request, 'teamowawa.html', {'carousel_images': carousel_images})


def upload_image(request):
    if request.method == 'POST':
        form = CarouselImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('url_del_carrusel')  # Redirige a la página del carrusel después de cargar la imagen
    else:
        form = CarouselImageForm()
    return render(request, 'upload_image.html', {'form': form})










