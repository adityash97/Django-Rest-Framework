from rest_framework import serializers
from watchlist_app.models import Movie

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

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer method field. Calculate something on the basis of method field and 
    return as a field from serializer.
    """
    name_length = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = '__all__'
        
    def get_name_length(self,obj):
        return len(obj.name)
        