from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out API View """
    name = serializers.CharField(max_length=50)