from netbox.api.routers import NetBoxRouter
from .views import *

router = NetBoxRouter()
router.register('impact', ImpactViewSet)
urlpatterns = router.urls