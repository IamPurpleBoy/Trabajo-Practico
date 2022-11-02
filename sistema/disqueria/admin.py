from re import A
from django.contrib import admin
from .models import Formato
from .models import Discografica
from .models import Interprete
from .models import Genero
from .models import Album, Tema




# Register your models here.
admin.site.register(Formato)
admin.site.register(Discografica)
admin.site.register(Interprete)
admin.site.register(Genero)
admin.site.register(Album)
admin.site.register(Tema)