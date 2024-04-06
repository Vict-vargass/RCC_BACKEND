from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Cliente, Pyme, Sucursal, Historial_asistencia, Servicio, Redes_sociale, Informacion_pyme, Redpoints_Ahorro
import bcrypt

class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['id','url', 'nombre', 'direccion', 'pyme']

# class ImagenesDescuentoSerializer(serializers.HyperlinkedModelSerializer):
#     imagen = Base64ImageField(required = False)
#     class Meta:
#         model = Imagenes_descuento
#         fields = ['id','url', 'imagen', 'descuento']

class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    # imagenes = ImagenesDescuentoSerializer(many=True, read_only=True)
    class Meta:
        model = Servicio
        fields = ['url','nombre', 'descripcion', 'porcentaje', 'valor', 'pyme']


class DescuentoResumenSerializer(serializers.HyperlinkedModelSerializer):
    # imagenes = ImagenesDescuentoSerializer(many=True, read_only=True)
    class Meta:
        model = Servicio
        fields = ['url','porcentaje', 'valor', 'pyme']

class AsistenciaSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Historial_asistencia
        fields = ['url','rut_cliente', 'pyme', 'monto_ahorrado', 'fecha', 'descuento']

class RedesSocialesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Redes_sociale
        fields = ['url','pyme', 'red_social', 'link']

class informacionPymeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Informacion_pyme
        fields = ['descripcion', 'horarios', 'direccion', 'pyme']

class PymeSerializer(serializers.HyperlinkedModelSerializer):
    sucursales = SucursalSerializer(many=True, read_only=True)
    servicios = ServicioSerializer(many=True, read_only=True)
    redes_sociales = RedesSocialesSerializer(many=True, read_only=True)
    informacion = informacionPymeSerializer(read_only=True)
    asistentes = AsistenciaSerializer(many=True, read_only=True)
    imagen = Base64ImageField(required = False)
    class Meta:
        model = Pyme
        fields = ['url', 'rut', 'nombre', 'imagen','correo', 'telefono', 'estado', 'password','servicios', 'sucursales','redes_sociales', 'informacion','asistentes', ]
    def to_representation(self, instance):
        # Sobrescribe el método para encriptar la contraseña en respuestas GET
        data = super(PymeSerializer, self).to_representation(instance)
        if 'password' in data:
            password = data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            data['password'] = hashed_password.decode('utf-8')
        return data

class AllPymeSerializer(serializers.HyperlinkedModelSerializer):
    sucursales = SucursalSerializer(many=True, read_only=True)
    servicios = ServicioSerializer(many=True, read_only=True)
    redes_sociales = RedesSocialesSerializer(many=True, read_only=True)
    informacion = informacionPymeSerializer(read_only=True)
    asistentes = AsistenciaSerializer(many=True, read_only=True)
    class Meta:
        model = Pyme
        fields = ['url', 'rut', 'nombre', 'correo', 'telefono','servicios', 'estado' 'sucursales','redes_sociales', 'informacion','asistentes', ]

class RedpointsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Redpoints_Ahorro
        fields = ['monto_ahorrado','redpoints', 'cliente']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    imagen = Base64ImageField(required = False)
    asistencias = AsistenciaSerializer(many=True, read_only= True)
    redpoints_ahorro = RedpointsSerializer(read_only= True)
    class Meta:
        model = Cliente
        fields = ['url', 'rut', 'nombre', 'apellido', 'correo','telefono', 'estado','imagen','password', 'redpoints_ahorro', 'asistencias']

    def to_representation(self, instance):
        # Sobrescribe el método para encriptar la contraseña en respuestas GET
        data = super(ClienteSerializer, self).to_representation(instance)
        if 'password' in data:
            password = data['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            data['password'] = hashed_password.decode('utf-8')
        return data
    


class AllClienteSerializer(serializers.HyperlinkedModelSerializer):
    asistencias = AsistenciaSerializer(many=True, read_only= True)
    class Meta:
        model = Cliente
        fields = ['url', 'rut', 'nombre', 'apellido', 'correo','telefono','asistencias']
