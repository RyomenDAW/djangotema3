from django.shortcuts import render
from .models import Libro
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_libros(request):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros = libros.all()
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libro(request, id_libro):
    libro = Libro.objects.select_related("biblioteca").prefetch_related("autores").get(id=id_libro)
    return render(request, 'libro/libro.html',{"libro_mostrar":libro})

def dame_libro_fecha(request,anyo_libro,mes_libro):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros = libros.filter(fecha_publicacion__year=anyo_libro,fecha_publicacion__month=mes_libro)
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})

def dame_libros_idioma(request, idioma):
    libros = Libro.objects.select_related("biblioteca").prefetch_related("autores")
    libros = libros.filter(Q(idioma=idioma) | Q(idioma="ES")).order_by("fecha_publicacion")
    return render(request, 'libro/lista.html',{"libros_mostrar":libros})
