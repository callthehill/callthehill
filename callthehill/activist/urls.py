from activist.views import ActivistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activist', ActivistViewSet)
urlpatterns = router.urls
