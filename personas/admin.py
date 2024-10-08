from django.contrib import admin
from .models import Biblioteca, Libro, Autor, DatosCliente, Cliente
admin.site.register(Biblioteca)
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(DatosCliente)
admin.site.register(Cliente)

# Register your models here.
