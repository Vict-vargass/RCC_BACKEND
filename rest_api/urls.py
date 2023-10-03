from django.urls import path, include
from rest_framework import routers
from rest_api import views

router = routers.DefaultRouter()
router.register(r'cliente', views.ClienteViewSet)
router.register(r'pyme', views.PymeViewSet)
router.register(r'sucursal', views.SucursalViewSet)
router.register(r'descuento', views.DescuentoViewSet)
router.register(r'asistencia', views.AsistenciaViewSet)

urlpatterns=[
    path('', include(router.urls))
]