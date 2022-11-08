import statistics
from django.http import Http404
from .models import *
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        usuario_data = request.data

        new_usuario = Usuario.objects.create(uid=usuario_data["uid"])
        new_usuario.save()

        for coords in usuario_data["ubicacion"]:
            new_latlng = LatLng.objects.create(
                latitud=coords["latitud"], longitud=coords["longitud"])
            new_usuario.ubicacion.add(new_latlng)

        serializer = UsuarioSerializer(new_usuario)

        return Response(serializer.data)
    def delete(self):
        id_usuario = self.kwargs['id']
        return Usuario.objects.filter(id=id_usuario).delete()



class UsuarioSearchSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        uid_usuario = self.kwargs['uid']
        return Usuario.objects.filter(uid=uid_usuario)
     
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=statistics.HTTP_204_NO_CONTENT)
    


class UsuarioDeleteSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        id_usuario = self.kwargs['id']
        return Usuario.objects.filter(id=id_usuario).delete()
