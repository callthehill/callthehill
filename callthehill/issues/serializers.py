from issues.models import *
from rest_framework import serializers

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
