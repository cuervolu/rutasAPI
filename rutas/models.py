from django.db import models

# Create your models here.

class Origen(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
class Destino(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
class Pasajero(models.Model):
    uid = models.CharField(max_length=200)

class Rutas(models.Model):
    direccion = models.CharField(max_length=500)
    chofer = models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)
    origen = models.OneToOneField(Origen,on_delete=models.CASCADE)
    destino = models.OneToOneField(Destino,on_delete=models.CASCADE)
    pasajero = models.OneToOneField(Pasajero,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.direccion