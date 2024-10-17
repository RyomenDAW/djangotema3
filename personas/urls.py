"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('libros/listar',views.listar_libros,name='lista_libros'),
    path("libros/<int:id_libro>/", views.dame_libro,name="dame_libro"),
    path("libros/listar/<int:anyo_libro>/<int:mes_libro>", views.dame_libro_fecha, name="dame_libros_fecha"),
    path("libros/listar/<str:idioma>/", views.dame_libros_idioma,name="dame_libros_idioma")
]