from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import Album, Interprete, Formato, Discografica, Genero
from .forms import AlbumForm
from .forms import InterpreteForm
from .forms import FormatoForm
from .forms import DiscograficaForm
from .forms import GeneroForm

# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')
    
def albums(request):
    print(request.GET)
    albums = Album.objects.all().order_by('nombre')
    print(albums)
    return render(request,'albums/index.html', {'albums': albums})

def buscarAlbum(request):
    busqueda = request.GET.get('Buscar')
    print(busqueda)
    albumsName = Album.objects.filter(nombre__icontains = busqueda).order_by('nombre')
    return render(request,'albums/por-nombre.html', {'buscarAlbums': albumsName})
    
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


def interpretes(request):
    interprete = Interprete.objects.all()
    print(interprete)
    return render(request,'interprete/info.html', {'interpretes': interprete})

def crearInterprete(request):
    formulario= InterpreteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('interprete')
    return render(request,'interprete/crear.html', {'formulario': formulario})   

def editarInterprete(request, id_interprete):
    interprete= Interprete.objects.get(id_interprete=id_interprete)
    formulario= InterpreteForm(request.POST or None, request.FILES or None, instance=interprete)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('interprete')
    return render(request,'interprete/editar.html', {'formulario': formulario})

def borrarInterprete(request, id_interprete):
    interprete= Interprete.objects.get(id_interprete=id_interprete)
    interprete.delete()
    return redirect('interprete')


def formatos(request):
    formato = Formato.objects.all().order_by('tipo')
    print(formato)
    return render(request,'formato/info.html', {'formatos': formato})
    
def crearFormato(request):
    formulario= FormatoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('formato')
    return render(request,'formato/crear.html', {'formulario': formulario})   

def editarFormato(request, id_formato):
    formato= Formato.objects.get(id_formato=id_formato)
    formulario= FormatoForm(request.POST or None, request.FILES or None, instance=formato)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('formato')
    return render(request,'formato/editar.html', {'formulario': formulario})

def borrarFormato(request, id_formato):
    formato= Formato.objects.get(id_formato=id_formato)
    formato.delete()
    return redirect('formato')



def discograficas(request):
    discografica = Discografica.objects.all().order_by('nombre')
    print(discografica)
    return render(request,'discografica/info.html', {'discograficas': discografica})
    
def crearDiscografica(request):
    formulario= DiscograficaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('discografica')
    return render(request,'discografica/crear.html', {'formulario': formulario})   

def editarDiscografica(request, id_discografica):
    discografica= Discografica.objects.get(id_discografica = id_discografica)
    formulario= DiscograficaForm(request.POST or None, request.FILES or None, instance=discografica)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('discografica')
    return render(request,'discografica/editar.html', {'formulario': formulario})

def borrarDiscografica(request, id_discografica):
    discografica= Discografica.objects.get(id_discografica = id_discografica)
    discografica.delete()
    return redirect('discografica')



def generos(request):
    genero = Genero.objects.all().order_by('nombre')
    print(genero)
    return render(request,'genero/info.html', {'generos': genero})
    
def crearGenero(request):
    formulario= GeneroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('genero')
    return render(request,'genero/crear.html', {'formulario': formulario})   

def editarGenero(request, id_genero):
    genero= Genero.objects.get(id_genero=id_genero)
    formulario= GeneroForm(request.POST or None, request.FILES or None, instance=genero)
    if formulario.is_valid() and request.POST:
        genero.save()
        return redirect('genero')
    return render(request,'genero/editar.html', {'formulario': formulario})

def borrarGenero(request, id_genero):
    genero= Genero.objects.get(id_genero=id_genero)
    genero.delete()
    return redirect('genero')