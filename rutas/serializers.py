from rest_framework import serializers
from .models import *

class OrigenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origen
        fields = '__all__'
class DestinoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destino
        fields = '__all__'
class WayPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = '__all__'
class PasajeroSerializer(serializers.ModelSerializer):
    waypoint = WayPointSerializer(many=True)
    class Meta:
        model = Pasajero
        fields = '__all__'

class RutasSerializer(serializers.ModelSerializer):
    origen = OrigenSerializer()
    destino = DestinoSerializer()
    pasajero = PasajeroSerializer(many=True)
    class Meta:
        model = Rutas
        fields = ('__all__')
        read_only_fields = ('fecha',)
        depth = 2
        
    
        
    