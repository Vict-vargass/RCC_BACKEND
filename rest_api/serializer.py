from rest_framework import serializers
from .models import Cliente, Pyme, Sucursal, Asistencia_Pyme, Descuento


class PymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pyme
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia_Pyme
        fields = ['url','rut_cliente', 'pyme', 'monto_ahorrado', 'fecha']


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    asistencias = AsistenciaSerializer(many=True, read_only= True)
    class Meta:
        model = Cliente
        fields = ['url','correo', 'rut', 'nombre', 'apellido', 'telefono', 'estado', 'password','asistencias']