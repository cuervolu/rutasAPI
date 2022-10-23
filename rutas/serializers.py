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


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = '__all__'


class RutasSerializer(serializers.ModelSerializer):
    origen = OrigenSerializer()
    class Meta:
        model = Rutas
        fields = ('__all__')
        read_only_fields = ('fecha',)
        depth = 2
        
    