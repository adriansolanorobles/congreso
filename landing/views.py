from django.shortcuts import render,redirect,  get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template


from .forms import AsistentesForm, PonentesForm
# Create your views here.
def index(request):
	return render(request, 'landing/index.html')

def registro(request):
	return render(request, 'landing/registro.html')	

def invitacion(request):
	return render(request, 'landing/invitacion.html')	

def programa(request):
	return render(request, 'landing/programa.html')
def convocatoria(request):
	return render(request, 'landing/convocatoria.html')

def comite_organizador(request):
	return render(request, 'landing/comite_organizador.html')

def ponentes_new(request):
	form = PonentesForm(request.POST or None)
	return render(request, 'landing/ponentes_new.html', {'form':form})

def asistentes_new(request):
	form = AsistentesForm(request.POST or None)

	return render(request, 'landing/asistentes_new.html', {'form':form})


def ponentes_create(request):
	
	form = PonentesForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			ponentes = form.save()
			ponentes.folio = '1CIPCHV-​P' + str(ponentes.id)
			ponentes.save()	
			ctx = {}
			to = []
			ctx['nombre_completo'] = ponentes.a1_nombre + ' ' + ponentes.a1_apellido_paterno + ' ' + ponentes.a1_apellido_materno
			ctx['folio'] = ponentes.folio
			to.append(ponentes.a1_correo_electronico)

			from_email = 'notificaciones@habilidadesparaadolescentes.com'
			subject = '1er. Congreso Internacional de Psicología Contemplativa y Habilidades para la Vida'
			bcc = ['seldor492@gmail.com','jorge_alfamar@hotmail.com']
			body = get_template('landing/correo_ponentes.html').render(ctx)
			msg = EmailMessage(subject=subject, body=body, to=to, 
			from_email=from_email,
			bcc = bcc
			)
			msg.content_subtype = 'html'
			msg.send()

			return render(request, 'landing/confirmacion_ponente.html',{'nombre_completo':ctx['nombre_completo'],'folio': ctx['folio'] })

	return redirect("landing:index")

def asistentes_create(request):
	
	form = AsistentesForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			asistentes = form.save()
			asistentes.folio = '1CIPCHV-​A' + str(asistentes.id)
			asistentes.save()	
			ctx = {}
			to = []
			ctx['nombre_completo'] = asistentes.nombre + ' ' + asistentes.apellido_paterno + ' ' + asistentes.apellido_materno
			ctx['folio'] = asistentes.folio
			to.append(asistentes.correo_electronico)

			from_email = 'notificaciones@habilidadesparaadolescentes.com'
			subject = '1er. Congreso Internacional de Psicología Contemplativa y Habilidades para la Vida'
			bcc = ['seldor492@gmail.com','jorge_alfamar@hotmail.com']
			body = get_template('landing/correo_asistentes.html').render(ctx)
			msg = EmailMessage(subject=subject, body=body, to=to, 
			from_email=from_email,
			bcc = bcc
			)
			msg.content_subtype = 'html'
			msg.send()	
			return render(request, 'landing/confirmacion_asistente.html',{'nombre_completo':ctx['nombre_completo'],'folio': ctx['folio'] })	

	return redirect("landing:index")