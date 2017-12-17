from django.shortcuts import render
from .forms import AsistenteForm
# Create your views here.
def index(request):
	return render(request, 'landing/index.html')	

def acerca_de(request):
	return render(request, 'landing/acerca_de.html')
"""
def ponentes_new(request):
	form = PonenteForm(request.POST or None)
	return render(request, 'landing/ponentes_new.html', {'form':form})
"""
def asistentes_new(request):
	form = AsistenteForm(request.POST or None)
	return render(request, 'landing/asistentes_new.html', {'form':form})