from cgitb import html
from contextlib import _RedirectStream
from distutils.command.build import build
import email
import string
from webbrowser import get

from django.contrib import messages
from django.contrib import redirects
from django.contrib.auth.decorators import login_required

from pedidos.models import LineaPedido, Pedido

from carro.carro import Carro
from tienda.models import Producto

from django.template.loader import render_to_string

from django.utils.html import strip_tags

from django.core.mail import send_mail

@login_required(login_url="/autenticacion/logear")

def procesar_pedido(request):

    pedido=Pedido.objects.create(user=request.user)

    carro=Carro(request)
    lineas_pedido= list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

          producto_id=key, 
          cantidad=value["cantidad"],
          user=request.user,
          pedido=pedido,

        ))


    # Almacenamos en base de datos LineaPedido
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=request.user.email,
        nombreusuario=request.user.username,
        emailusuario= request.user.email
    )

    messages.success(request, "El pedido se ha creado correctamente")

    return redirects("../tienda")


def enviar_mail(**kwargs):

    asunto= "Gracias por su compra"

    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
    })

    mensaje_texto=strip_tags(mensaje)

    from_email="vielmatica@gmail.com"
    #to= kwargs.get("emailusuario")
    to="vielmatica@gmail.com"
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)




