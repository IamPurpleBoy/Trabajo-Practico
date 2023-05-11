from django import forms
from .models import *

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        
        fields = [ 
        'cod_album',
        'nombre',
        'id_interprete',
        'id_genero', 
        'cant_temas',
        'id_discografica',
        'id_formato',
        'fec_lanzamiento',
        'precio',
        'cantidad',
        'caratula',
        ] 


        widgets = {
            'cod_album' : forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'id_interprete' : forms.Select(attrs={'class': 'form-control'}),
            'id_genero' : forms.Select(attrs={'class': 'form-control'}),
            'cant_temas' : forms.NumberInput(attrs={'class': 'form-control'}),
            'id_discografica' : forms.Select(attrs={'class': 'form-control'}),
            'id_formato' : forms.Select(attrs={'class': 'form-control'}),
            'fec_lanzamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'caratula': forms.FileInput(attrs={'class': 'form-control'}),
        }

class InterpreteForm(forms.ModelForm):
  
    class Meta:
        model = Interprete
        
        fields = [ 
                        
            'nombre',    
            'apellido',
            'nacionalidad',
            'foto',
        ] 

        
        widgets = {
            
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad' : forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FormatoForm(forms.ModelForm):
  
    class Meta:
        model = Formato
        
        fields = [ 
                        
            'tipo',    
        
        ] 

        
        widgets = {
            
            'tipo' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class DiscograficaForm(forms.ModelForm):
  
    class Meta:
        model = Discografica
        
        fields = [ 
                        
            'nombre',    
        
        ] 

        
        widgets = {
            
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class GeneroForm(forms.ModelForm):
  
    class Meta:
        model = Genero
        
        fields = [ 
                        
            'nombre',    
        
        ] 

        
        widgets = {
            
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }


class TemaForm(forms.ModelForm):
  
    class Meta:
        model = Tema
        
        fields = [ 
                        
            'titulo',    
            'duracion',
            'autor',
            'compositor',
            'cod_album',
            'id_interprete',
        ] 

        
        widgets = {
            
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'duracion' : forms.TimeInput(attrs={'class': 'form-control'}),
            'autor' : forms.TextInput(attrs={'class': 'form-control'}),
            'compositor': forms.TextInput(attrs={'class': 'form-control'}),
            'cod_album': forms.Select(attrs={'class': 'form-control'}),
            'id_interprete': forms.Select(attrs={'class': 'form-control'}),
        
        }