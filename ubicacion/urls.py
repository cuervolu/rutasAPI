from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register(r'api/ubicacion', UsuarioViewSet, 'usuarios')
router.register(r'^api/ubicacion/(?P<id>.+)/$', UsuarioSearchSet, 'buscar'),



urlpatterns = router.urls
