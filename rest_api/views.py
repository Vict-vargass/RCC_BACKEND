from rest_framework import viewsets, status
from .serializer import ClienteSerializer, AllClienteSerializer
from .models import Cliente, Administrador
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your views here.

@permission_classes((IsAuthenticated,))
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# ---- VERIFICAR QUE UN USUARIO ES ACTIVO ----

@api_view(['POST'])
def userCheckStatus(request):
    user = request.data.get('user')
    try:
        usuario = Cliente.objects.get(correo=user)
        if usuario.estado == True:
            return Response({'isActive': True}, status= status.HTTP_200_OK)
        else:
            return Response({'isActive': False}, status= status.HTTP_403_FORBIDDEN)
    except:
        return Response({'exist': False}, status= status.HTTP_404_NOT_FOUND)

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def getClientes(request):
    pymes = Cliente.objects.all()
    serializer = AllClienteSerializer(pymes, many=True, context={'request': request})
    return Response(serializer.data)


# ---- FUNCIONES DE LOGIN PARA USUARIOS Y PYMES -----

@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def loginUser(request):
    user = request.data.get('user')
    password = request.data.get('password')
    usuario = Cliente.objects.get(rut=user)
    try:
        usuario = Cliente.objects.get(rut=user)
        if usuario.is_active:
            if usuario.password == password:
                return Response({'status': True, "hasAccess": True}, status= status.HTTP_202_ACCEPTED)
            else:
                return Response({'exist': True, 'hasAccess': True, 'pass': False}, status= status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'hasAccess': False}, status= status.HTTP_403_FORBIDDEN)
    except:
        return Response({'exist': False}, status= status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def AdminLogin(request):
    username = request.data.get('user')
    password = request.data.get('password')
    
    try:
        user = Administrador.objects.get(username=username)

        if check_password(password, user.password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'estado': True, "hasAccess": True, 'Token': token.key}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'hasAccess': True, 'pass': False}, status=status.HTTP_401_UNAUTHORIZED)
    except Administrador.DoesNotExist:
        return Response({'exist': False}, status=status.HTTP_404_NOT_FOUND)

