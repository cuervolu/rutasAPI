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
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["waypoint"] = WayPointSerializer(instance.waypoint.all(), many=True).data
        return rep    
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class ChoferSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()
    class Meta:
        model = Chofer
        fields = '__all__'
class RutasSerializer(serializers.ModelSerializer):
    origen = OrigenSerializer()
    destino = DestinoSerializer()
    pasajero = PasajeroSerializer(many=True)
    chofer = ChoferSerializer()
    class Meta:
        model = Rutas
        fields = ('__all__')
        depth = 5
        
    
        
    