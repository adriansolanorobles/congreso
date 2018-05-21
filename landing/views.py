from django.shortcuts import render,redirect,  get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.template import Context
from django.template.loader import render_to_string, get_template
from .models import asistentes


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

def announcement(request):
	return render(request, 'landing/announcement.html')

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
			subject = 'Confirmación de registro - Ponente'
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
	numero_de_personas_registradas = 0
	form = AsistentesForm(request.POST, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			asistentes_object = form.save(commit=False)
			numero_de_personas_registradas = asistentes.objects.filter(talleres_disponibles=asistentes_object.talleres_disponibles).count()
			if numero_de_personas_registradas <= 35:

				asistentes_object.folio = '1CIPCHV-​A' + str(asistentes_object.id)
				asistentes_object.save()	
				ctx = {}
				to = []
				ctx['nombre_completo'] = asistentes_object.nombre + ' ' + asistentes_object.apellido_paterno + ' ' + asistentes_object.apellido_materno
				ctx['folio'] = asistentes_object.folio
				to.append(asistentes_object.correo_electronico)

				from_email = 'notificaciones@habilidadesparaadolescentes.com'
				subject = 'Confirmación de registro - Asistente'
				bcc = ['seldor492@gmail.com','jorge_alfamar@hotmail.com']
				body = get_template('landing/correo_asistentes.html').render(ctx)
				msg = EmailMessage(subject=subject, body=body, to=to, 
				from_email=from_email,
				bcc = bcc
				)
				msg.content_subtype = 'html'
				msg.send()	
				return render(request, 'landing/confirmacion_asistente.html',{'nombre_completo':ctx['nombre_completo'],'folio': ctx['folio'] })
			else:
				return render(request, 'landing/sobrecupo_asistente.html')	

	return redirect("landing:index")