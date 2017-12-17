from django.conf.urls import url, include

from .views import index, asistentes_new#, ponentes_new

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^asistentes_new/$', asistentes_new,name="asistentes_new"),
#	url(r'^ponentes_new/$', ponentes_new,name="ponentes_new"),
	

]