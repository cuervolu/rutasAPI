from .models import *
from rest_framework import viewsets, permissions
from .serializers import RutasSerializer
from rest_framework.response import Response


class RutasViewSet(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = RutasSerializer

    def create(self, request, *args, **kwargs):
        ruta_data = request.data

        new_origen = Origen.objects.create(
            latitud=ruta_data["origen"]["latitud"], longitud=ruta_data["origen"]["longitud"])
        new_origen.save()

        new_destino = Destino.objects.create(
            latitud=ruta_data["destino"]["latitud"], longitud=ruta_data["destino"]["longitud"])
        new_destino.save()

        new_pasajero = Pasajero.objects.create(
            uid=ruta_data["pasajero"]["uid"])
        new_destino.save()

        new_ruta = Rutas.objects.create(direccion=ruta_data['direccion'],
                                        chofer=ruta_data['chofer'],
                                        origen=new_origen, destino=new_destino,
                                        pasajero=new_pasajero)
        new_ruta.save()

        serializer = RutasSerializer(new_ruta)

        return Response(serializer.data)
