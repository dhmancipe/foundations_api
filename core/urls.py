from rest_framework.routers import DefaultRouter
from .views import EventViewSet, FoundationViewSet

router = DefaultRouter()
router.register("foundations", FoundationViewSet)
router.register("events", EventViewSet)
urlpatterns = router.urls