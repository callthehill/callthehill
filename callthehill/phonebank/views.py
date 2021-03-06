from rest_framework import viewsets
from phonebank.models import Call
from phonebank.serializers import CallSerializer


class CallViewSet(viewsets.ModelViewSet):
    """
    Allows for creation, update, deletion, and listing of Calls
    """
    queryset = Call.objects.all()
    serializer_class = CallSerializer
