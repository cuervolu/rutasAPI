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

        new_vehiculo = Vehiculo.objects.create(
            marca=ruta_data["chofer"]["vehiculo"]["marca"], anio=ruta_data["chofer"]["vehiculo"]["anio"], modelo=ruta_data["chofer"]["vehiculo"]["modelo"])

        new_chofer = Chofer.objects.create(
            uid=ruta_data["chofer"]["uid"], vehiculo=new_vehiculo)

        new_ruta = Rutas.objects.create(direccion=ruta_data["direccion"], 
                                        precio=ruta_data["precio"], 
                                        fecha=ruta_data["fecha"],
                                        chofer=new_chofer,
                                        origen=new_origen, destino=new_destino)
        new_ruta.save()

        for pasajero in ruta_data["pasajero"]:
            new_pasajero = Pasajero.objects.create(
                uid=pasajero["uid"])

            new_ruta.pasajero.add(new_pasajero)

        for waypoint in ruta_data["pasajero"]:
            new_waypoint = Waypoint.objects.create(
                latitud=waypoint["waypoint"]["latitud"], longitud=waypoint["waypoint"]["longitud"])
            new_pasajero.waypoint.add(new_waypoint)

        serializer = RutasSerializer(new_ruta)

        return Response(serializer.data)


class RutasSearchSet(viewsets.ModelViewSet):
    serializer_class = RutasSerializer

    def get_queryset(self):
        id_ruta = self.kwargs['id']
        return Rutas.objects.filter(id=id_ruta)


class RutaDeleteSet(viewsets.ModelViewSet):
    serializer_class = RutasSerializer

    def get_queryset(self):
        id_ruta = self.kwargs['id']
        return Rutas.objects.filter(id=id_ruta).delete()
