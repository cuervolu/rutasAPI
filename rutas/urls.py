from rest_framework import routers
from .api import RutasViewSet, RutasSearchSet
from ubicacion.urls import router as ubicacion_router
router = routers.DefaultRouter()

router.register(r'api/rutas', RutasViewSet, 'rutas')
router.register(r'^api/rutas/(?P<id>.+)/$', RutasSearchSet, 'buscar'),
router.registry.extend(ubicacion_router.registry)

urlpatterns = router.urls
