from rest_framework import serializers

item_types = ["update", "new-legislation", "issue"]

class FeedItemSerializer(serializers.Serializer):
    """
    An item to display in the feed
    """
    item_type = serializers.ChoiceField(choices=item_types)
    title = serializers.CharField()
    blurb = serializers.CharField()
    action = serializers.URLField()
