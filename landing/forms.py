# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import asistentes

class AsistenteForm( forms.ModelForm ):
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

