from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from .models import Producto, Categoria  # Importa el modelo de productos



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = authenticate(request, email=email)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {email}!')
                return redirect('login.html')  
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')



def categoria_monitores(request):
    return render(request, 'categoria_monitores.html')

def categoria_muebles(request):
    return render(request, 'categoria_muebles.html')


def categoria_celulares(request):
    # Filtra los productos de la categoría "Celulares"
    productos_celulares = Producto.objects.filter(codigo_categoria__categoria='Celulares')
    # Pasa los productos a la plantilla
    context = {
        'productos_celulares': productos_celulares,
    }
    return render(request, 'categoria_celulares.html', context)

def carrito(request):
    return render(request, 'carrito.html')

def cuenta(request):
    return render(request, 'cuenta.html')
