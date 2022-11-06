from rest_framework import routers
from .api import RutasViewSet, RutasSearchSet

router = routers.DefaultRouter()

router.register(r'api/rutas', RutasViewSet, 'rutas')
router.register(r'^api/rutas/(?P<id>.+)/$', RutasSearchSet, 'buscar'),

urlpatterns = router.urls
