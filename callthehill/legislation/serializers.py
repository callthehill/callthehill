from legislation.models import *
from rest_framework import serializers

class LegislatorSerializer(serializers.ModelSerializer):
    """
    A very basic serializer for a Legislator
    """
    class Meta:
        model = Legislator
        fields = "__all__"

class HonorificSerializer(serializers.ModelSerializer):
    """
    A very basic serializer for an Honorific
    """
    class Meta:
        model = Honorific
        fields = "__all__"

class PronounsSerializer(serializers.ModelSerializer):
    """
    A very basic serializer for a Pronoun
    """
    class Meta:
        model = Pronouns
        fields = "__all__"

class PartySerializer(serializers.ModelSerializer):
    """
    A very basic serializer for a Party
    """
    class Meta:
        model = Party
        fields = "__all__"

class BodySerializer(serializers.ModelSerializer):
    """
    A very basic serializer for a Body
    """
    class Meta:
        model = Body
        fields = "__all__"

class VoteSerializer(serializers.ModelSerializer):
    """
    A very basic serializer for a Vote
    """
    class Meta:
        model = Vote
        fields = "__all__"

class LegislationSerializer(serializers.ModelSerializer):
    """
    A very basic serializer for a Legislation
    """
    class Meta:
        model = Legislation
        fields = "__all__"
