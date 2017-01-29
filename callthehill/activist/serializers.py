from activist.models import Activist
from rest_framework import serializers

class ActivistSerializer(serializers.ModelSerializer):
    """
    A serialized Activist
    """
    class Meta:
        model = Activist
        fields = ("name", "location", "zip_code", "interests", "photo", "id", )
        read_only_fields = ("photo", "id", )
        