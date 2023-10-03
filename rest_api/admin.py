from django.contrib import admin
from .models import Cliente, Pyme, Sucursal, Asistencia_Pyme, Descuento
# Register your models here.


admin.site.register(Cliente)
admin.site.register(Pyme)
admin.site.register(Sucursal)
admin.site.register(Asistencia_Pyme)
admin.site.register(Descuento)
