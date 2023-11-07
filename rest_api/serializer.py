from rest_framework import serializers
from .models import Cliente, Pyme, Sucursal, Asistencia_Pyme, Descuento, Redes_sociale, informacion_pyme


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['url', 'nombre', 'pyme']

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = ['url','nombre', 'descripcion', 'porcentaje','pyme']

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia_Pyme
        fields = ['url','rut_cliente', 'pyme', 'monto_ahorrado', 'fecha']


class RedesSocialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redes_sociale
        fields = ['url','pyme', 'red_social', 'link']


class informacionPymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = informacion_pyme
        fields = ['descripcion', 'horarios', 'direccion', 'pyme']

class PymeSerializer(serializers.HyperlinkedModelSerializer):
    sucursales = SucursalSerializer(many=True, read_only=True)
    descuentos = DescuentoSerializer(many=True, read_only=True)
    redes_sociales = RedesSocialesSerializer(many=True, read_only=True)
    informacion = informacionPymeSerializer(read_only=True)
    class Meta:
        model = Pyme
        fields = ['url', 'rut', 'nombre', 'correo', 'telefono', 'password','descuentos', 'sucursales','redes_sociales', 'informacion']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    asistencias = AsistenciaSerializer(many=True, read_only= True)
    class Meta:
        model = Cliente
        fields = ['url','correo', 'rut', 'nombre', 'apellido', 'telefono', 'estado', 'password','asistencias']