from django.contrib import admin
from .models import Articulo

# Register your models here.
#Forma1
#admin.site.register(Articulo)
#Forma2
@admin.register(Articulo) #Decorador: siempre tiene debajo una funcion o una clase
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo','imagen','autor')
