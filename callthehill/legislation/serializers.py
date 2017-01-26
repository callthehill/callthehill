from legislation.models import *
from rest_framework import serializers

class LegislatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legislator
        fields = "__all__"

class HonorificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honorific
        fields = "__all__"

class PronounsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronouns
        fields = "__all__"

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = "__all__"

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"

class LegislationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legislation
        fields = "__all__"
