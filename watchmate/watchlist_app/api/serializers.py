from pyexpat import model
from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform

# serializers.Serializer
"""
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    # on create(post)
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    # on update(put)
    def update(self,instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

"""

# Model Serializer

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        