from django.db import models

# Create your models here.
class Rutas(models.Model):
    origenLatLng = models.CharField(max_length=100)
    destino = models.CharField(max_length=500)
    destinoLatLng = models.CharField(max_length=100)
    chofer = models.CharField(max_length=150)
    pasajeros = models.TextField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
