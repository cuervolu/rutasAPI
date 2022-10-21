from .models import *
from rest_framework import viewsets, permissions
from .serializers import RutasSerializer


class RutasViewSet(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = RutasSerializer
