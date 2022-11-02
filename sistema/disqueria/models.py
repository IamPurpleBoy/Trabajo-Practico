from django.db import models

# Create your models here.
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

class Interprete(models.Model):     

    
        id_interprete = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50, verbose_name='nombre')
        apellido = models.CharField(max_length=50, verbose_name='apellido')
        nacionalidad = models.CharField(max_length=50, verbose_name='nacionalidad')
        foto = models.ImageField(upload_to='imagenes/', verbose_name='foto', null=True)

        def nombre_completo(self):
                return "{} {}" .format(self.nombre, self.apellido)

        def __str__(self) -> str:
                fila = self.nombre_completo()       
                return fila


        def delete(self, using=None, keep_parents=False ):
                self.foto.storage.delete(self.foto.name) 
                super().delete()
   
    

    
#---------------------------------------------------------------------------------------

class Genero(models.Model):
    
        id_genero = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=50, verbose_name='nombre')

        def __str__(self) -> str:
                fila =  self.nombre
                return fila

        def delete(self, using=None, keep_parents=False ):
                super().delete()
    


#---------------------------------------------------------------------------------------

class Discografica(models.Model):
   
    id_discografica = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='nombre')

    def __str__(self) -> str:
        fila =  self.nombre
        return fila

    def delete(self, using=None, keep_parents=False ):
        super().delete()
   

#---------------------------------------------------------------------------------------

class Formato(models.Model):
    id_formato=models.AutoField(primary_key=True)
    tipo= models.CharField(max_length=50, verbose_name='tipo')

    def __str__(self) -> str:
        fila = self.tipo 
        return fila

    def delete(self, using=None, keep_parents=False ):
        super().delete()




#---------------------------------------------------------------------------------------    

class Album(models.Model):
        
        id_album = models.AutoField(primary_key=True)
        cod_album = models.IntegerField(verbose_name='Código')
        nombre = models.CharField(max_length=50, verbose_name='Nombre')
        id_interprete = models.ForeignKey(Interprete, on_delete=models.DO_NOTHING, verbose_name='Intérprete')
        id_genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING, verbose_name='Género')
        cant_temas = models.IntegerField(verbose_name='Cantidad de temas')
        id_discografica = models.ForeignKey(Discografica,on_delete=models.DO_NOTHING, verbose_name='Discográfica')
        id_formato = models.ForeignKey(Formato, on_delete=models.DO_NOTHING, verbose_name='Formato')
        fec_lanzamiento = models.DateField(verbose_name='Lanzamiento')
        precio = models.DecimalField(max_digits=9, decimal_places=2 ,verbose_name='Precio')
        cantidad = models.IntegerField(verbose_name='Cantidad')
        caratula = models.ImageField(upload_to='imagenes/', verbose_name='Carátula', null=True) 

        def __str__(self) -> str:
            fila = self.nombre 
            return fila

        def delete(self, using=None, keep_parents=False ):
            self.caratula.storage.delete(self.caratula.name)    
            super().delete()

#---------------------------------------------------------------------------------------

class Tema(models.Model):
    
        id_tema = models.AutoField(primary_key=True)
        titulo = models.CharField(max_length=50, verbose_name='titulo')
        duracion = models.TimeField(verbose_name='duracion')
        autor = models.CharField(max_length=50, verbose_name='autor')
        compositor = models.CharField(max_length=50, verbose_name='compositor')
        cod_album = models.ForeignKey(Album, on_delete=models.DO_NOTHING)
        id_interprete = models.ForeignKey(Interprete, on_delete=models.DO_NOTHING)

        def __str__(self) -> str:
                fila = self.titulo
                return fila

        def delete(self, using=None, keep_parents=False ):
                super().delete()