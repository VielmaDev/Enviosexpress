from xml.dom.minidom import Document

from django.urls import path
from.views import VRegistro, cerrar_sesion, logear

urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('logear',logear, name="logear"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
   
]

