# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import asistentes, ponentes

class AsistentesForm( forms.ModelForm ):
	class Meta:
		model = asistentes
		fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'correo_electronico', 'telefono', 'institucion_de_procedencia', 'talleres_disponibles']
		widgets = {
			'nombre' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Nombre'} ),
			'apellido_paterno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido materno'} ),
			'apellido_materno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido paterno'} ),
			'correo_electronico' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Correo electrónico'} ),
			'telefono' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Telefono'} ),
			'institucion_de_procedencia' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Institución de Procedencia'} ),
			'talleres_disponibles' : forms.Select( attrs = {'class':'form-control',} ),

		}


class PonentesForm( forms.ModelForm ):
	class Meta:
		model = ponentes
		fields = ['titulo','a1_nombre', 'a1_apellido_paterno', 'a1_apellido_materno', 'a1_correo_electronico', 'a1_telefono', 'a1_institucion_de_procedencia', 'a2_nombre', 'a2_apellido_paterno', 'a2_apellido_materno', 'a3_nombre', 'a3_apellido_paterno', 'a3_apellido_materno', 'documento']
		widgets = {
			'titulo' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Título de la ponencia'} ),
			'a1_nombre' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Nombre'} ),
			'a1_apellido_paterno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido materno'} ),
			'a1_apellido_materno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido paterno'} ),
			'a1_correo_electronico' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Correo electrónico'} ),
			'a1_telefono' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Telefono'} ),
			'a1_institucion_de_procedencia' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Institución de Procedencia'} ),
			'a2_nombre' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Nombre'} ),
			'a2_apellido_paterno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido materno'} ),
			'a2_apellido_materno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido paterno'} ),
			'a3_nombre' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Nombre'} ),
			'a3_apellido_paterno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido materno'} ),
			'a3_apellido_materno' : forms.TextInput( attrs = {'class':'form-control', 'placeholder':'Apellido paterno'} ),
			'documento' : forms.ClearableFileInput( attrs = {'class':'form-control', 'placeholder':'Documento'} ),

		}