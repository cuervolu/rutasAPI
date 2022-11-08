from rest_framework import serializers
from .models import *


class LatLngSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatLng
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    ubicacion = LatLngSerializer(many=True)

    class Meta:
        model = Usuario
        fields = '__all__'

    def update(self, instance, validated_data):
        ubicacion = validated_data.pop('ubicacion', [])
        instance.uid = validated_data.get('uid', instance.uid)
        instance = super().update(instance, validated_data)
        ubicacion_objs = []
        for ubicacion_data in ubicacion:
            if "id" in ubicacion_data.keys():
                if LatLng.objects.filter(id=ubicacion["id"]).exists():
                    ubicacion = LatLng.objects.get(**ubicacion_data)
                    ubicacion_objs.append(ubicacion)
                else: 
                   continue
            else:
                latlng = LatLng.objects.create(**ubicacion_data)
                ubicacion_objs.append(latlng)
        instance.ubicacion.set(ubicacion_objs)        
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["ubicacion"] = LatLngSerializer(
            instance.ubicacion.all(), many=True).data
        return rep
