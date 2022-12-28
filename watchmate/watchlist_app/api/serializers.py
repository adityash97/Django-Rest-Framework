from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields ='__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'



class StreamPlatformSerializer(serializers.ModelSerializer):
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    '''The field name should be the : "related_name" of model field. As in this case it is : "watchlist" '''
    watchlist = WatchListSerializer(many=True, read_only = True)
    '''Control nested field''' 
    # only name will show
    # watchlist = serializers.StringRelatedField(many=True,read_only=True)
    #only pk will show
    # watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # link to page will show 
    # watchlist = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='watchlist_details')
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        