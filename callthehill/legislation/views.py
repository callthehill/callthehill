from rest_framework import viewsets
from legislation.models import *
from legislation.serializers import *


class LegislatorViewSet(viewsets.ModelViewSet):
    queryset = Legislator.objects.all()
    serializer_class = LegislatorSerializer

class HonorificViewSet(viewsets.ModelViewSet):
    queryset = Honorific.objects.all()
    serializer_class = HonorificSerializer

class PronounsViewSet(viewsets.ModelViewSet):
    queryset = Pronouns.objects.all()
    serializer_class = PronounsSerializer

class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class LegislationViewSet(viewsets.ModelViewSet):
    queryset = Legislation.objects.all()
    serializer_class = LegislationSerializer
