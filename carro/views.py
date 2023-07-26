from django.shortcuts import render

from django.shortcuts import redirect
from .carro import Carro
from tienda.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):

    carro= Carro(request)

    productos= Producto.objects.get(id= producto_id)

    carro.agregar(producto=productos)

    return redirect("tienda")


def eliminar_producto(request, producto_id):

    carro= Carro(request)

    productos= Producto.objects.get(id= producto_id)

    carro.eliminar(producto= productos)

    return redirect("tienda")


def restar_producto(request, producto_id):

    carro= Carro(request)

    productos= Producto.objects.get(id= producto_id)

    carro.restar_producto(producto= productos)

    return redirect("tienda")

def limpiar_carro(request):

    carro= Carro(request)

    carro.limpiar_carro()

    return redirect("tienda")








