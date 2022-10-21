from dataclasses import fields
from rest_framework import serializers
from .models import *

class RutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = '__all__'
        read_only_fields =('fecha',) 