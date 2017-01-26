from phonebank.views import CallViewSet 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'call', CallViewSet)

urlpatterns = router.urls
