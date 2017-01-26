from legislation.views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'legislator', LegislatorViewSet)
router.register(r'honorific', HonorificViewSet)
router.register(r'pronouns', PronounsViewSet)
router.register(r'party', PartyViewSet)
router.register(r'body', BodyViewSet)
router.register(r'vote', VoteViewSet)
router.register(r'legislation', LegislationViewSet)


urlpatterns = router.urls
