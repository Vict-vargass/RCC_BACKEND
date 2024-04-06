from rest_framework import viewsets, status
from .serializer import PymeSerializer, SucursalSerializer, ServicioSerializer, AsistenciaSerializer, informacionPymeSerializer, RedesSocialesSerializer, AllPymeSerializer, AllClienteSerializer
from .models import Cliente, Pyme, Sucursal, Servicio, Historial_asistencia, Redes_sociale, Informacion_pyme
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
# Create your views here.

# ---- VIEWSET's PARA PYMES, SE NECESITA TOKEN PARA UTILIZAR

#@permission_classes((IsAuthenticated,))
class PymeViewSet(viewsets.ModelViewSet):
    queryset = Pyme.objects.all()
    serializer_class = PymeSerializer

#@permission_classes((IsAuthenticated,))
class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

#@permission_classes((IsAuthenticated,))
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

#@permission_classes((IsAuthenticated,))
class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Historial_asistencia.objects.all()
    serializer_class = AsistenciaSerializer

#@permission_classes((IsAuthenticated,))
class RedesSocialesViewSet(viewsets.ModelViewSet):
    queryset = Redes_sociale.objects.all()
    serializer_class = RedesSocialesSerializer

#@permission_classes((IsAuthenticated,))
class InfoPymesViewSet(viewsets.ModelViewSet):
    queryset = Informacion_pyme.objects.all()
    serializer_class = informacionPymeSerializer

#@permission_classes((IsAuthenticated,))
# class ImgDescuentoViewSet(viewsets.ModelViewSet):
#     queryset = Imagenes_descuento.objects.all()
#     serializer_class = ImagenesDescuentoSerializer

#@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def getPymes(request):
    pymes = Pyme.objects.all()
    serializer = AllPymeSerializer(pymes, many=True, context={'request': request})
    return Response(serializer.data)

#@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def createPyme(request):
    data = JSONParser().parse(request)
    serializer = PymeSerializer(data=data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def loginPyme(request):
    pyme = request.data.get('user')
    password = request.data.get('password')
    try:
        pyme = Pyme.objects.get(rut=pyme)
        if pyme.password == password:
            token, created = Token.objects.get_or_create(user=pyme)
            return Response({'estado': True, "hasAccess": True, 'Token': token.key}, status= status.HTTP_202_ACCEPTED)
        else:
            return Response({'hasAccess': True, 'pass': False}, status= status.HTTP_401_UNAUTHORIZED)
    except:
        return Response({'exist': False}, status= status.HTTP_404_NOT_FOUND)

