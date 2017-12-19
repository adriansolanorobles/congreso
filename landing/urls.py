from django.conf.urls import url, include

from .views import index, convocatoria, invitacion, registro, programa, asistentes_new, asistentes_create, ponentes_new

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^convocatoria/$', convocatoria, name='convocatoria'),
	url(r'^invitacion/$', invitacion, name='invitacion'),
	url(r'^programa/$', programa, name='programa'),
	url(r'^asistentes_new/$', asistentes_new,name="asistentes_new"),
	url(r'^asistentes/create/$', asistentes_create, name="asistentes_create"),
	url(r'^registro/$', registro,name="registro"),
	url(r'^ponentes_new/$', ponentes_new,name="ponentes_new"),
	

]