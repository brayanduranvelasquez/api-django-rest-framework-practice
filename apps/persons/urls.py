from rest_framework.routers import SimpleRouter
from .views import PersonApiViewSet

router = SimpleRouter()
router.register('', PersonApiViewSet)
