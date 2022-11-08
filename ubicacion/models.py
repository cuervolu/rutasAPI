from django.db import models

# Create your models here.

class LatLng(models.Model):
    latitud = models.FloatField();
    longitud = models.FloatField();
    def __str__(self):
        return str(self.latitud) + "," + str(self.longitud) 
    
    
class Usuario(models.Model):
    uid = models.CharField(max_length=150, blank=False, null=False);
    ubicacion = models.ManyToManyField(LatLng, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.uid