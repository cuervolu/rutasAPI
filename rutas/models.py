from django.db import models

# Create your models here.


class Origen(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    def __str__(self):
        return str(self.latitud) + "," + str(self.longitud) 

class Destino(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    def __str__(self):
        return str(self.latitud) + "," + str(self.longitud) 

class Waypoint(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    def __str__(self):
        return str(self.latitud) + "," + str(self.longitud) 
class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    anio = models.IntegerField(blank=False, null=False)
    modelo = models.CharField(max_length=50)
    def __str__(self):
        return self.marca + " " + str(self.anio) + " " + self.modelo

class Chofer(models.Model):
    uid = models.CharField(max_length=150)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.uid
class Pasajero(models.Model):
    uid = models.CharField(max_length=200)
    waypoint = models.ManyToManyField(Waypoint, blank=True)

    def __str__(self):
        return self.uid
class Rutas(models.Model):
    direccion = models.CharField(max_length=500)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    origen = models.OneToOneField(Origen, on_delete=models.CASCADE)
    destino = models.OneToOneField(Destino, on_delete=models.CASCADE)
    pasajero = models.ManyToManyField(Pasajero, related_name='pasajero')

    def __str__(self):
        return self.direccion
