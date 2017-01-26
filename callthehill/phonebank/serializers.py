from phonebank.models import Call
from rest_framework import serializers

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"
        read_only_fields = ("activist", )
        