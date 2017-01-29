from rest_framework import viewsets
from issues.models import *
from issues.serializers import *

class IssueViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Issues
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer