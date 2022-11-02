from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album
from .forms import AlbumForm
# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')
    
def albums(request):
    albums = Album.objects.all()
    return render(request,'albums/index.html', {'albums': albums})
    
def crearAlbum(request):
    formulario= AlbumForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('albums')
    return render(request,'albums/crear.html', {'formulario': formulario})   

def editarAlbum(request, id_album):
    album= Album.objects.get(id_album=id_album)
    formulario= AlbumForm(request.POST or None, request.FILES or None, instance=album)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('albums')
    return render(request,'albums/editar.html', {'formulario': formulario})

def borrarAlbum(request, id_album):
    album= Album.objects.get(id_album=id_album)
    album.delete()
    return redirect('albums')