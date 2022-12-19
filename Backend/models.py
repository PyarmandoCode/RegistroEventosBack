from django.db import models
from django.contrib.auth.models import User

class Cia(models.Model):
    cia_id = models.AutoField(primary_key=True)
    cia_nombre_corto = models.CharField(max_length=10)
    cia_nombre = models.CharField(max_length=250)
    cia_usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # todo administrador de CIA = CRUD
    #departamentos = models.ManyToManyField(Departamentos)
    cia_fechacrea = models.DateTimeField(auto_now_add=True)
    cia_state = models.BooleanField(default=True)

    def __str__(self):
        return self.cia_nombre

    class Meta:
        db_table = "Cia"


class Areas(models.Model):
    areas_id = models.AutoField(primary_key=True)
    area_nombre_corto = models.CharField(max_length=250)
    area_nombre = models.CharField(max_length=250)
    cia = models.ForeignKey(Cia, on_delete=models.CASCADE)
    area_usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # todo administrador de CIA = CRUD
    area_fechacrea = models.DateTimeField(auto_now_add=True)
    area_state = models.BooleanField(default=True)

    def __str__(self):
        return self.area_nombre

    class Meta:
        db_table = "Areas"
        verbose_name_plural = "Areas"

class Empleados(models.Model):

    empleados_tipo = (
        ('Operador','Operador'),
        ('Admin', 'Admin'),
        ('SuperUsuario', 'SuperUsuario'),
    )
    empleado_id = models.AutoField(primary_key=True)
    empleado_nombre_corto = models.CharField(max_length=50)
    empleado_nombre = models.CharField(max_length=250)
    empleado_celular = models.CharField(max_length=50)
    empleado_tipo = models.CharField(max_length=90,choices=empleados_tipo, blank=True, null=True)
    cia = models.ForeignKey(Cia, on_delete=models.CASCADE)
    #estacionamiento = models.OneToOneField(Estacionamiento, on_delete=models.CASCADE, blank=True, null=True)
    empleado_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    empleado_fechacrea = models.DateTimeField(auto_now_add=True)
    empleado_state = models.BooleanField(default=True)

    def __str__(self):
        return self.empleado_nombre

    class Meta:
        db_table = "Empleados"
        verbose_name_plural = "Empleados"


class Eventos(models.Model):
    eventos_id = models.AutoField(primary_key=True)
    eventos_nombre = models.CharField(max_length=50,blank=True,null=True)
    cia = models.ForeignKey(Cia, on_delete=models.CASCADE)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    evento_descripcion = models.TextField()
    eventos_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    eventos_fechacrea = models.DateTimeField(auto_now_add=True)
    eventos_state = models.BooleanField(default=True)

    def __str__(self):
        return self.evento_descripcion

    class Meta:
        db_table = "Eventos"
        verbose_name_plural = "Eventos"



