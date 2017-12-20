from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import os
import time
# Create your models here.

TALLERES = {
    (1,'La Práctica de la Plena Consciencia en el Salón de Clases.'),
    (2,'Manejo del Estrés en la Tutoría Individual y Grupal través de la Atención Plena.'),
    (3,'Estrategias Docentes para el Desarrollo de Habilidades para la Vida.'),
    (4,'Grupos Cooperativos para el Desarrollo de Habilidades Sociales en el Aula.'),
    (5,'Desarrollo del Pensamiento Crítico a través de la Filosofía para Niños.'),
    (6,'El Debate como Estrategia Didáctica para Desarrollar Habilidades Argumentativas en los Estudiantes.'),
    (7,'Aplicación del Aprendizaje Basado en Proyectos en el Salón de Clases.'),
    (8,'Aplicación en el Aula del Aprendizaje Basado en Problemas a través de la Historia de Casos.'),
    (9,'El uso del Portafolio como Estrategia de Enseñanza y Evaluación.'),
    (10,'Habilidades Contemplativas, Género y Violencia.'),
}

LINEAS_TEMATICAS = (
    (1,'Análisis teórico (CCAT)'),
    (2,'Investigación empírica en educación (CCIE)'),
    (3,'Investigación empírica en la salud (CCIS)'),
    (4,'Análisis teórico sobre el desarrollo de habilidades para la vida. (HVAT)'),
    (5,'Estrategias de enseñanza y desarrollo de habilidades para la vida (IEHVE)'),
    (6,'Habilidades socioemocionales (IEHSE)'),
    (7,'Habilidades cognoscitivas (IEHC)'),
    (8,'Habilidades de investigación en ciencias(IEHIC)'),
    (9,'Habilidades de investigación en humanidades (IEHIH)'),
    (10,'Evaluación de habilidades para la vida (IEEHV)'),

)
class asistentes(models.Model):
    folio = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=255)
    institucion_de_procedencia = models.CharField(max_length=255)
    talleres_disponibles = models.IntegerField(choices=TALLERES)

    class Meta:
        ordering = ('nombre',)
        verbose_name= 'Asistentes'

    def __str__(self):
        return '{0} {1}'.format(self.nombre,self.apellido_paterno)


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s_%s.%s" % (instance.a1_nombre, instance.a1_apellido_paterno, str(int(round(time.time()*1000))), ext)
    return os.path.join('archivos/', filename)

class ponentes(models.Model):
    olio = models.CharField(max_length=255, blank=True, null=True)
    lineas_tematicas = models.IntegerField(choices=LINEAS_TEMATICAS)
    titulo = models.CharField(max_length=255)   
    a1_nombre = models.CharField(max_length=255)
    a1_apellido_paterno = models.CharField(max_length=255)
    a1_apellido_materno = models.CharField(max_length=255)
    a1_correo_electronico = models.EmailField()
    a1_telefono = models.CharField(max_length=255)
    a1_institucion_de_procedencia = models.CharField(max_length=255) 
    a2_nombre = models.CharField(max_length=255)
    a2_apellido_paterno = models.CharField(max_length=255)
    a2_apellido_materno = models.CharField(max_length=255)
    a3_nombre = models.CharField(max_length=255)
    a3_apellido_paterno = models.CharField(max_length=255)
    a3_apellido_materno = models.CharField(max_length=255)
    documento = models.FileField(upload_to=content_file_name)

    class Meta:
        ordering = ('titulo',)
        verbose_name= 'Ponentes'

    def __str__(self):
        return '{0} {1}'.format(self.nombre,self.apellido_paterno)    

#****************************Usuario****************************************************
class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')
        email = self.normalize_email(email)

        user = self.model(email=email,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):
    # unique, no se van a repetir
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido_paterno = models.CharField(max_length=100, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=100, verbose_name='Apellido Materno')
    email = models.EmailField(unique=True,verbose_name='Correo Electrónico')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # intermediario entre trans de cada modelo, object managaer de cada modelo
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.nombre.encode('utf8') + ' ' + self.apellido_paterno.encode('utf8') + ' ' + self.apellido_materno.encode('utf8')  
 
#********************************************************************************************
