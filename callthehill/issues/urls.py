from issues.views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'issue', IssueViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = router.urls
