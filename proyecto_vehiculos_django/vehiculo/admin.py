from django.contrib import admin
from django.contrib.auth.models import User, Permission

# Register your models here.
from .models import Vehiculo

admin.site.register(Vehiculo)
admin.site.register(Permission)

admin.site.unregister(User)  # Desregistrando el modelo User predeterminado

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # Verificar si es un nuevo usuario
            obj.save()  # Guardar el nuevo usuario
            # Asignar permiso de acceso al panel de administración al nuevo usuario
            admin_permission = Permission.objects.get(codename='add_logentry')
            obj.user_permissions.add(admin_permission)
        else:
            obj.save()  # Guardar el usuario existente sin cambios en los permisos

admin.site.register(User, CustomUserAdmin)  # Registrando el modelo User personalizado