from phonebank.models import Call
from rest_framework import serializers

class CallSerializer(serializers.ModelSerializer):
    """
    A serializer for Call.
    Does not allow for modification of the Activist, always the logged-in user.
    """
    class Meta:
        model = Call
        fields = "__all__"
        read_only_fields = ("activist", )
        