from rest_framework import serializers
from movielist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    
class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    rate = serializers.IntegerField()
    description = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)