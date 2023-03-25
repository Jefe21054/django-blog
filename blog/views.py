from django.shortcuts import render,redirect
from .models import Articulo,Comentario

# Create your views here.
def index(request):
    
    listaArticulos = Articulo.objects.all()

    print(listaArticulos)

    context = {
        'articulos':listaArticulos
    } 

    return render(request,'blog/index.html',context)

def contenido(request,articulo_id):

    objArticulo = Articulo.objects.get(pk=articulo_id)
    listaComentarios = Comentario.objects.filter(articulo=objArticulo)

    context = {
        'articulo':objArticulo,
        'comentarios':listaComentarios
    }

    return render(request,'blog/articulo.html',context)

def comentar(request,articulo_id):

    if request.method == 'POST':
        
        objArticulo = Articulo.objects.get(pk=articulo_id)

        comentario = request.POST['comentario']
        print(comentario)
        nuevoComentario = Comentario()
        nuevoComentario.texto = comentario
        nuevoComentario.articulo = objArticulo
        nuevoComentario.save()

    return redirect('/contenido/'+str(articulo_id))

    
