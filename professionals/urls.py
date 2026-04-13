from rest_framework.routers import DefaultRouter

from .views import ProfessionalViewSet

router = DefaultRouter()
router.register(r"professionals", ProfessionalViewSet)

urlpatterns = router.urls
