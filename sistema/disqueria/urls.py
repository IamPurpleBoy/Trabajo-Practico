#from django.urls import pathfrom unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('albums', views.albums, name='albums'),
    path('crear/albums', views.crearAlbum, name='crear'),
    path('editar/albums', views.editarAlbum, name='editar'),
    path('borrar/albums/<int:id_album>', views.borrarAlbum, name='borrar'),
    path('editar/albums/<int:id_album>', views.editarAlbum, name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)