#from django.urls import pathfrom unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('albums', views.albums, name='albums'),
    path('albums/por-nombre', views.buscarAlbum, name='buscarAlbum'),
    path('crear/albums', views.crearAlbum, name='crearAlbum'),
    path('editar/albums', views.editarAlbum, name='editarAlbum'),
    path('borrar/albums/<int:id_album>', views.borrarAlbum, name='borrarAlbum'),
    path('editar/albums/<int:id_album>', views.editarAlbum, name='editarAlbum'),
    path('interprete', views.interpretes, name='interprete'),
    path('editar/interprete', views.editarInterprete, name='editarInterprete'),
    path('borrar/interprete/<int:id_interprete>', views.borrarInterprete, name='borrarInterprete'),
    path('editar/interprete/<int:id_interprete>', views.editarInterprete, name='editarInterprete'),
    path('crear/interprete',views.crearInterprete, name='crearInterprete'),
    path('formato', views.formatos, name='formato'),
    path('crear/formato', views.crearFormato, name='crearFormato'),
    path('editar/formato', views.editarFormato, name='editarFormato'),
    path('borrar/formato/<int:id_formato>', views.borrarFormato, name='borrarFormato'),
    path('editar/formato/<int:id_formato>', views.editarFormato, name='editarFormato'),
    path('discografica', views.discograficas, name='discografica'),
    path('crear/discografica', views.crearDiscografica, name='crearDiscografica'),
    path('editar/discografica', views.editarDiscografica, name='editarDiscografica'),
    path('borrar/discografica/<int:id_discografica>', views.borrarDiscografica, name='borrarDiscografica'),
    path('editar/discografica/<int:id_discografica>', views.editarDiscografica, name='editarDiscografica'),
    path('genero', views.generos, name='genero'),
    path('crear/genero', views.crearGenero, name='crearGenero'),
    path('editar/genero', views.editarGenero, name='editarGenero'),
    path('borrar/genero/<int:id_genero>', views.borrarGenero, name='borrarGenero'),
    path('editar/genero/<int:id_genero>', views.editarGenero, name='editarGenero'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)