from xml.dom.minidom import Document
from django.urls import path
from .import views

urlpatterns = [
    path('blog', views.blog, name="blog"),
    path('categoria/<int:categoria_id>', views.categoria, name="categoria"),
]