from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    date = serializers.DateField()
    email = serializers.EmailField(max_length=100)


    

    
