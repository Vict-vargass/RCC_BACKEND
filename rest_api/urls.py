from django.urls import path, include
from rest_framework import routers
from rest_api import viewset_pyme, views
from rest_api.views import loginUser
from rest_api.viewset_pyme import loginPyme, getPymes, createPyme
from rest_api.views import loginUser, AdminLogin

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'pyme', viewset_pyme.PymeViewSet)
router.register(r'sucursal', viewset_pyme.SucursalViewSet)
router.register(r'descuento', viewset_pyme.DescuentoViewSet)
router.register(r'asistencia', viewset_pyme.AsistenciaViewSet)
router.register(r'info-pymes', viewset_pyme.InfoPymesViewSet)
router.register(r'redes-sociales-pyme', viewset_pyme.RedesSocialesViewSet)
router.register(r'imagen-descuento-pyme', viewset_pyme.ImgDescuentoViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('login-pyme/', loginPyme, name="pyme_login"),
    path('login-user/', loginUser, name="user_login"),
    path('login-user/', loginUser, name="user_login"),
    path('pymes/', getPymes, name="pymes"),
    path('new-pyme/', createPyme, name="new_pyme"),
    path('login-admin/', AdminLogin, name="admin-login")
]
