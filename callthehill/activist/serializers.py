from activist.models import Activist
from rest_framework import serializers

class IssueCardSerializer(serializers.Serializer):
    pass

class NewLegislationCardSerializer(serializers.Serializer):
    pass

class UpdateCardSerializer(serializers.Serializer):
    pass

class ActivistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activist
        fields = ("name", "location", "zip_code", "interests", )
        read_only_fields = ("photo", "user_id", )
        