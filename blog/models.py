from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Articulo(models.Model):
    
    CATEGORIA_CHOICES = (
        ('General','General'),
        ('Diseño Web','Diseño Web'),
        ('Programación','Programación')
    )
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(default='')
    contenido = models.TextField(default='')
    duracion = models.IntegerField(default=0)
    fecha_registro = models.DateField(default=date.today)
    categoria = models.CharField(max_length=50,default='general',choices=CATEGORIA_CHOICES)
    imagen = models.ImageField(upload_to='articulos',blank=True)
    autor = models.ForeignKey(User,on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo,on_delete=models.RESTRICT)
    texto = models.TextField(default='')
    autor = models.CharField(max_length=255,default='Anónimo')

    def __str__(self):
        return self.autor
