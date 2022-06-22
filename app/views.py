from urllib import request
from django.http import response
from django.shortcuts import render,redirect

# Create your views here.

import requests
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,'app/index.html')

#SECCION AGREGAR PRODUCTO
def agregarpr(request):
    datos = {
        'form' : Productoform()
    }
    if request.method == 'POST' :
        formulario = Productoform (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')


    return render(request,'app/agregarpr/agregarpr.html', datos)

def listarpr(request):
    #SE SACA ESTO DE LA TIENDA YA QUE ES EL CICLO FOR
    # ASI MANDAMOS LOS MISMOS DATOS AL LISTAR CON EL JASON (DATOS)
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/listarpr/listarpr.html',datos)

#CAMBIAR LOS ID POR CODIGO
def modificarpr(request,codigo):
    # SECCION MODIFICAR
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : Productoform(instance=producto)
    }
    if request.method == 'POST':
        formulario = Productoform(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto modificado correctamente!')
            datos['form'] = formulario

    return render(request, 'app/modificarpr/modificarpr.html', datos)

# SECCION ELIMINAR
def eliminarproducto(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarpr")

def carrito(request):
    carritoAll = Carrito.objects.all()
    datos = {
        'listaCarrito' : carritoAll
    }

    if request.method == 'POST':
        carrito = Carrito.objects.all().delete()

    return render(request, 'app/carrito.html', datos)


def tienda(request):
    response = requests.get('http://127.0.0.1:8000/api/productos/').json()
    response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
    response3 = requests.get('https://rickandmortyapi.com/api/character/1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183').json()

    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll,
        'listaJson' : response,
        'listaDigimon': response2,
        'listaRrmorty' : response3
    }
    if request.method == 'POST':
        tipoProducto = TipoProducto()
        tipoProducto.tipo = request.POST.get('tipo')

        producto = Producto()
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.tipo = tipoProducto
        producto.imagen = request.POST.get('imagen')
        carrito = Carrito()
        carrito.codigo = producto
        carrito.save()
        

    return render(request,'app/tienda/Tiendaprincipal.html',datos)

def nosotros(request):
    return render(request,'app/nosotros/nosotros.html')

def pago(request):
    return render(request,'app/pago/pago.html')

def donacion(request):
    return render(request,'app/donacion/suspago.html')




def registro(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/register.html', datos)

def seguimiento(request):
    return render(request,'app/seguimiento/seguimiento.html')

def perfil(request):
    return render(request,'app/perfil/perfil.html')

def suscribirse(request):
    return render(request, 'app/suscripcion/suscripcion.html')

def historial(request):
    return render(request,'app/historial/historial.html')

def ventas(request):
    return render(request, 'app/ventas/ventas.html')

