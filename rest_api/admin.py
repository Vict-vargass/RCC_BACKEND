from django.contrib import admin
from .models import Cliente, Pyme, Sucursal, Asistencia_Pyme, Descuento, informacion_pyme, Redes_sociale
# Register your models here.


admin.site.register(Cliente)
admin.site.register(Pyme)
admin.site.register(Sucursal)
admin.site.register(Asistencia_Pyme)
admin.site.register(Descuento)
admin.site.register(Redes_sociale)
admin.site.register(informacion_pyme)
