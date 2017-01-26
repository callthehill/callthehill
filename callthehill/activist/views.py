from activist.models import Activist
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from activist.serializers import ActivistSerializer

class ActivistViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for editing and viewing Activists
    """

    queryset = Activist.objects.all()
    serializer_class = ActivistSerializer


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        