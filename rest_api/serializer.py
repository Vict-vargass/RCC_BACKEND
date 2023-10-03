from rest_framework import serializers
from .models import Cliente, Pyme, Sucursal, Asistencia_Pyme, Descuento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'correo', 'telefono', 'estado', 'password',]

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
        fields = '__all__'