from rest_framework import viewsets
from .serializer import ClienteSerializer, PymeSerializer, SucursalSerializer, DescuentoSerializer, AsistenciaSerializer
from .models import Cliente, Pyme, Sucursal, Descuento, Asistencia_Pyme
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PymeViewSet(viewsets.ModelViewSet):
    queryset = Pyme.objects.all()
    serializer_class = PymeSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia_Pyme.objects.all()
    serializer_class = AsistenciaSerializer
