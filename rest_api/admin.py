from django.contrib import admin
from .models import Cliente, Pyme, Sucursal, Historial_asistencia, Descuento, Informacion_pyme, Redes_sociale, Administrador
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# admin.py
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['username', 'correo', 'is_staff', 'is_superuser']  # Ajusta según tus campos
    list_filter = ['is_staff', 'is_superuser']  # Ajusta según tus campos


# Registra el modelo Administrador con la clase AdministradorAdmin personalizada
admin.site.register(Administrador, AdministradorAdmin)


admin.site.register(Cliente)
admin.site.register(Pyme)
admin.site.register(Sucursal)
admin.site.register(Historial_asistencia)
admin.site.register(Descuento)
admin.site.register(Redes_sociale)
admin.site.register(Informacion_pyme)
