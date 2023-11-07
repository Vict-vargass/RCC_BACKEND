from rest_framework import viewsets, status
from .serializer import ClienteSerializer, PymeSerializer, SucursalSerializer, DescuentoSerializer, AsistenciaSerializer, informacionPymeSerializer, RedesSocialesSerializer
from .models import Cliente, Pyme, Sucursal, Descuento, Asistencia_Pyme, Redes_sociale, informacion_pyme
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    @action(detail=False, methods=['post'])
    def login(self, request):
        user = request.data.get('user')
        password = request.data.get('password')
        try:
            usuario = Cliente.objects.get(rut=user)
            if usuario.estado != False:
                if(usuario.password == password):
                    return Response({'estado': True, "hasAccess": True}, status= status.HTTP_202_ACCEPTED)
                else:
                    return Response({'exist': True, 'hasAccess': True, 'pass': False}, status= status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'hasAccess': False}, status= status.HTTP_403_FORBIDDEN)
        except:
            return Response({'exist': False}, status= status.HTTP_404_NOT_FOUND)


class PymeViewSet(viewsets.ModelViewSet):
    queryset = Pyme.objects.all()
    serializer_class = PymeSerializer
    def login(self, request):
        user = request.data.get('user')
        password = request.data.get('password')
        try:
            pyme = Pyme.objects.get(rut=user)
            if pyme.password == password:
                return Response({'estado': True, "hasAccess": True}, status= status.HTTP_202_ACCEPTED)
            else:
                return Response({'hasAccess': True, 'pass': False}, status= status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'exist': False}, status= status.HTTP_404_NOT_FOUND)


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class DescuentoViewSet(viewsets.ModelViewSet):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia_Pyme.objects.all()
    serializer_class = AsistenciaSerializer

class RedesSocialesViewSet(viewsets.ModelViewSet):
    queryset = Redes_sociale.objects.all()
    serializer_class = RedesSocialesSerializer

class InfoPymesViewSet(viewsets.ModelViewSet):
    queryset = informacion_pyme.objects.all()
    serializer_class = informacionPymeSerializer