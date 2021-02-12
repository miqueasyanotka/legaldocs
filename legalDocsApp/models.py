from django.db import models

# Create your models here.

class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    contrasenia = models.CharField(max_length=100)

class Escribano(Usuarios):
    idEscribano = models.AutoField(primary_key=True)
    matricula = models.IntegerField(max_length=6)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()
    piso = models.CharField(max_length=50, blank=True)
    numeroPuerta = models.CharField(blank=True)

class Cliente(Usuarios):
    idCliente = models.AutoField(primary_key=True)

class Turno(models.Model):
    idTurno = models.AutoField(primary_key=True)
    fecha = models.DateTimeField('%Y-%m-%d %H:%M')
    Escribano_idEscribano = models.ForeignKey(Escribano, on_delete=models.CASCADE)
    Cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Documento(models.Model):
    idDocumento = models.AutoField(primary_key=True)
    paginas = models.IntegerField()
    tipo = models.CharField(max_length=100)
    Cliente_idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Escribano_idEscribano = models.ForeignKey(Escribano, on_delete=models.CASCADE)