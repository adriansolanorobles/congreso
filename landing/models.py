from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

TALLERES = {
    (1,'Taller 1'),
    (2,'Taller 2'),
    (3,'Taller 3'),
}
class asistentes(models.Model):
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

#class ponentes(models.Model):
    


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
