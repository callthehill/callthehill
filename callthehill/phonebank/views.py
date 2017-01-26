from rest_framework import viewsets
from phonebank.models import Call
from phonebank.serializers import CallSerializer


class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
