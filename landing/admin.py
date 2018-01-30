from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from .models import User
from .models import ponentes, asistentes

# Register your models here.

class UserAdmin(UA):
    fieldsets = (
        ('Datos de Cuenta', {
            'fields': ('email', 'password', 'is_active', 'is_staff','is_superuser')
        }), ('Datos personales', {
            'fields': ('nombre', 'apellido_paterno', 'apellido_materno')

        }),
        (('Permissions'), {'fields': ('groups', 'user_permissions')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    def username(self, instance):
        return instance.email

    def user_first_name(self, instance):
        return instance.nombre

    def user_last_name(self, instance):
        return instance.apellido_paterno

    list_display = ('email', 'user_first_name', 'user_last_name', 'is_active')
    ordering = ('email',)


class PonentesAdmin(admin.ModelAdmin):
    pass


class AsistentesAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(ponentes, PonentesAdmin)
admin.site.register(asistentes, AsistentesAdmin)