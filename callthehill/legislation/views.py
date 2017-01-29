from rest_framework import viewsets
from legislation.models import *
from legislation.serializers import *


class LegislatorViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Legislators
    """
    queryset = Legislator.objects.all()
    serializer_class = LegislatorSerializer

class HonorificViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Honorifics
    """
    queryset = Honorific.objects.all()
    serializer_class = HonorificSerializer

class PronounsViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Pronouns
    """
    queryset = Pronouns.objects.all()
    serializer_class = PronounsSerializer

class PartyViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Parties
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer

class BodyViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Bodies
    """
    queryset = Body.objects.all()
    serializer_class = BodySerializer

class VoteViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Votes
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

class LegislationViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Legislation
    """
    queryset = Legislation.objects.all()
    serializer_class = LegislationSerializer
