from django.shortcuts import render,redirect,  get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .forms import AsistentesForm
# Create your views here.
def index(request):
	return render(request, 'landing/index.html')	

def invitacion(request):
	return render(request, 'landing/invitacion.html')	

def programa(request):
	return render(request, 'landing/programa.html')
def convocatoria(request):
	return render(request, 'landing/convocatoria.html')
"""
def ponentes_new(request):
	form = PonenteForm(request.POST or None)
	return render(request, 'landing/ponentes_new.html', {'form':form})
"""
def asistentes_new(request):
	form = AsistentesForm(request.POST or None)
	return render(request, 'landing/asistentes_new.html', {'form':form})

def asistentes_create(request):
	
	form = AsistentesForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			asistentes = form.save()			

	return redirect("landing:index")