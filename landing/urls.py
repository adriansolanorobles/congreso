from django.conf.urls import url, include

from .views import index, convocatoria, asistentes_new, asistentes_create#, ponentes_new

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^convocatoria/$', convocatoria, name='convocatoria'),
	url(r'^asistentes_new/$', asistentes_new,name="asistentes_new"),
	url(r'^asistentes/create/$', asistentes_create, name="asistentes_create"),
#	url(r'^ponentes_new/$', ponentes_new,name="ponentes_new"),
	

]