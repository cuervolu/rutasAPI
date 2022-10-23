from rest_framework import routers
from .api import RutasViewSet

router = routers.DefaultRouter()

router.register(r'api/rutas', RutasViewSet, 'rutas')

urlpatterns = router.urls
