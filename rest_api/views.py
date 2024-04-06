from rest_framework import viewsets, status
from .serializer import ClienteSerializer, AllClienteSerializer, RedpointsSerializer
from .models import Cliente, Administrador, Redpoints_Ahorro
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.template.loader import render_to_string
from rest_framework.views import APIView
# Create your views here.

from django.core.mail import send_mail


# @permission_classes((IsAuthenticated,))
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class RPAhorroViewSet(viewsets.ModelViewSet):
    queryset = Redpoints_Ahorro.objects.all()
    serializer_class = RedpointsSerializer

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

#@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def getClientes(request):
    pymes = Cliente.objects.all()
    serializer = AllClienteSerializer(pymes, many=True, context={'request': request})
    return Response(serializer.data)


# ---- FUNCIONES DE LOGIN PARA USUARIOS Y PYMES -----

#@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def loginUser(request):
    user = request.data.get('user')
    password = request.data.get('password')
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



class Correos(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def Correo_de_bienvenida(self, request):
            asunto = 'Bienvenid@! a la comunidad'
            mensaje = "Probando"
            mensaje_html = render_to_string('email.html', {'variable': 'Hola mundo'})
            correo = "vgvs360@gmail.com"  # Puede ser una lista de correos
            # Envía el correo electrónico
            try:
                send_mail(
                    asunto,
                    mensaje,
                    'settings.EMAIL_HOST_USER',
                    [correo],
                    html_message=mensaje_html,
                    fail_silently=False
                )
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'mensaje': f'Error al enviar el correo: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods='POST')
    def Correo_de_recuperación(self):
            asunto = 'Correo de Prueba'
            mensaje = "Probando"
            mensaje_html = render_to_string('email.html', {'variable': 'Hola mundo'})
            correo = "vgvs360@gmail.com"  # Puede ser una lista de correos
            # Envía el correo electrónico
            try:
                send_mail(
                    asunto,
                    mensaje,
                    'settings.EMAIL_HOST_USER',
                    [correo],
                    html_message=mensaje_html,
                    fail_silently=False
                )
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'mensaje': f'Error al enviar el correo: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


