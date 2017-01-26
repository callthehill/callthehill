from activist.views import ActivistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activists', ActivistViewSet)

urlpatterns = router.urls
