# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import asistentes, ponentes

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

class PonenteForm(forms.ModelForm):
	id_padre = forms.ModelChoiceField(queryset=cat_cuentas.objects.all(), required=False, empty_label='', widget=forms.Select(attrs={'class':'form-control js-select2'}))
	
	class Meta:
		model = cat_cuentas
		fields = ['clave','descripcion', 'porcentaje', 'corrida', 'id_padre' ]
		widgets = {
			'clave': forms.TextInput(attrs= {'placeholder':'Clave','class':'form-control'}),
			'descripcion': forms.TextInput(attrs= {'placeholder':'Descripción','class':'form-control'}),
			'porcentaje': forms.TextInput(attrs= {'placeholder':'Porcentaje','class':'form-control'}),
			'corrida': forms.CheckboxInput(attrs= {'class':'custom-control-input'}),
			

		}