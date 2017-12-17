from django.conf.urls import url, include

from .views import index, acerca_de, asistentes_new#, ponentes_new

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^acerca_de/$', acerca_de, name='acerca_de'),
	url(r'^asistentes_new/$', asistentes_new,name="asistentes_new"),
#	url(r'^ponentes_new/$', ponentes_new,name="ponentes_new"),
	

]