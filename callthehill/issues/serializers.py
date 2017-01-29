from issues.models import *
from rest_framework import serializers

class IssueSerializer(serializers.ModelSerializer):
    """
    Very basic serializer for an Issue
    """
    class Meta:
        model = Issue
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    """
    Very basic serializer for a Tag
    """
    class Meta:
        model = Tag
        fields = "__all__"
