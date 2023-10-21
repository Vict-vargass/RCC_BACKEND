from django.db import models

class Cliente(models.Model):
    rut = models.CharField(primary_key= True, max_length=10, null=False)
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    correo =models.CharField(max_length=40, null= False)
    telefono= models.CharField(max_length=10, null=False)
    estado= models.BooleanField(null=False)
    password= models.CharField(max_length=15, null=False)
    def __str__(self):
        return'{}'.format(self.rut)    

class Pyme(models.Model):
    rut = models.CharField(primary_key=True, max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    correo =models.CharField(max_length=30, null= False)
    telefono= models.CharField(max_length=10, null=True)
    direccion = models.CharField(max_length=50, null=False)
    password= models.CharField(max_length=15, null=False)
    def __str__(self):
        return'{} {}'.format(self.nombre, self.rut)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    pyme = models.ForeignKey('Pyme', on_delete=models.CASCADE, db_column='pyme')
    def __str__(self):
        return'{} {}'.format(self.pyme, self.nombre)

class Descuento(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=1000, null=False)
    porcentaje = models.FloatField(null=False)
    pyme = models.ForeignKey('Pyme', on_delete=models.CASCADE, db_column='pyme')
    def __str__(self):
        return'{} {}'.format(self.pyme, self.nombre)

class Asistencia_Pyme (models.Model):
    rut_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='rut_cliente', related_name='asistencias')
    pyme = models.ForeignKey('Pyme', on_delete=models.CASCADE, db_column='pyme')
    monto_ahorrado = models.IntegerField( null=False)
    fecha = models.DateField(null=False)
    def __str__(self):
        return'{} {}'.format(self.rut_cliente, self.pyme)
