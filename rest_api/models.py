from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, m2m_changed

class AdministradorManager(BaseUserManager):
    def create_user(self, username, correo, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        if not password:
            raise ValueError('La contraseña es obligatoria para los usuarios normales')
        user = self.model(username=username, correo=correo, **extra_fields)
        user.password = make_password(password)  # Usa make_password para hashear la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, username, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, correo, password, **extra_fields)

class Administrador(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=1000)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AdministradorManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'correo'
    REQUIRED_FIELDS = ['correo']

    def __str__(self):
        return '{} {}'.format(self.username, self.correo)


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, null=False)
    correo = models.EmailField(max_length=100, null= False, unique=True)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    telefono= models.CharField(max_length=12, null=False)
    password= models.CharField(max_length=15, null=False)
    imagen = models.ImageField(blank=True, null=True, upload_to='RCC_BACKEND/static/cliente/')
    class Estados(models.TextChoices):
        Activo = "Activo"
        Inactivo = "Inactivo"
    estado = models.CharField(max_length=25, choices=Estados.choices)

    def __str__(self):
        return'{}'.format(self.rut)    


class Pyme(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    password= models.CharField(max_length=15, null=False)
    correo =models.CharField(max_length=30, null= False)
    telefono= models.CharField(max_length=12, null=True)
    
    class Estados(models.TextChoices):
        Activo = "Activo"
        Inactivo = "Inactivo"
    
    estado = models.CharField(max_length=25, choices=Estados.choices)
    imagen = models.ImageField(blank=True, null=True, upload_to='RCC_BACKEND/static/pyme/')


    def __str__(self):
        return'{} {}'.format(self.nombre, self.rut)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=200, null=False)
    pyme = models.ForeignKey('Pyme', on_delete=models.CASCADE, db_column='pyme', related_name='sucursales')
    def __str__(self):
        return'{} {}'.format(self.pyme, self.nombre)

class Servicio(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    porcentaje = models.FloatField(null=False)
    valor = models.IntegerField(null= False)
    pyme = models.ForeignKey('Pyme', on_delete=models.CASCADE, db_column='pyme', related_name='descuentos')
    def __str__(self):
        return'{} {}'.format(self.pyme, self.nombre)

# class Imagenes_descuento(models.Model):
#     imagen = models.ImageField(blank=True, null=True, upload_to='RCC_BACKEND/static/descuento/')
#     descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE, db_column='desc', related_name="imagenes")
#     def __str__(self):
#         return'{}'.format(self.descuento)

class Historial_asistencia (models.Model):
    rut_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, db_column='rut_cliente', related_name='asistencias')
    pyme = models.ForeignKey('Pyme', on_delete=models.CASCADE, db_column='pyme', related_name='asistentes')
    monto_ahorrado = models.IntegerField( null=True)
    fecha = models.DateField(null=False)
    descuento = models.ManyToManyField(Servicio)
    def __str__(self):
        return'{} {}'.format(self.rut_cliente, self.pyme)
    class Meta:
        ordering = ["-fecha", "-id"]

class Redes_sociale (models.Model):
    pyme = models.ForeignKey(Pyme, on_delete=models.CASCADE, db_column='pyme', related_name='redes_sociales')
    class redes(models.TextChoices):
        Instagram = "Instagram"
        Facebook = "Facebook"
        Twitter = "Twitter"
        Sitio_Web ="Sitio Web"
    red_social = models.CharField(max_length=25, choices=redes.choices)
    link = models.CharField(null=False, max_length=2000)
    def __str__(self):
        return'{}'.format(self.pyme)


class Informacion_pyme (models.Model):
    descripcion = models.CharField(null=False, max_length=4000)
    horarios = models.CharField(null=True, max_length=500)
    pyme = models.OneToOneField(Pyme, on_delete=models.CASCADE, db_column='pyme', related_name='informacion')
    direccion = models.CharField(max_length=50, null=False)
    def __str__(self):
        return'{}'.format(self.pyme)
    

class Redpoints_Ahorro (models.Model):
    monto_ahorrado = models.IntegerField(null=False)
    redpoints = models.IntegerField(null=True)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, db_column='cliente', related_name='redpoints_ahorro')
    def __str__(self):
        return'{}'.format(self.cliente)
    

@receiver(post_save, sender=Historial_asistencia)
def actualizar_redpoints_ahorro(sender, instance, created, **kwargs):

    try:
        rp = Redpoints_Ahorro.objects.get(cliente=instance.rut_cliente)
        rp.monto_ahorrado += instance.monto_ahorrado 
        rp.redpoints += instance.monto_ahorrado * 0.1
        rp.save()
            
    except:
        Redpoints_Ahorro.objects.update_or_create(cliente=instance.rut_cliente, 
                                                  defaults={'monto_ahorrado': instance.monto_ahorrado, 'redpoints': instance.monto_ahorrado * 0.1})



@receiver(post_save, sender=Cliente)
def crear_monto_ahorro(sender, instance, created, **kwargs):
    if created:
        try:
            rp = Redpoints_Ahorro.objects.create(monto_ahorrado=0, redpoints=0, cliente=instance)
            rp.save()
        except Exception as e:
            print("Error al crear Redpoints_Ahorro:", e)



@receiver(m2m_changed, sender=Historial_asistencia.descuento.through)
def actualizar_monto_ahorrado(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        # Recalcular el monto ahorrado
        monto_ahorrado = 0
        for servicio in instance.descuento.all():
            monto_ahorrado += servicio.valor * servicio.porcentaje / 100
        
        # Actualizar el monto ahorrado en la instancia de Historial_asistencia
        instance.monto_ahorrado = monto_ahorrado
        instance.save()
