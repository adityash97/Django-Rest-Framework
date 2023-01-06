from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movielist_app.models import Movie
from .serializers import MovieSerializer,ReviewSerializer

@api_view(['GET','POST'])
def movieList(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def movieDetails(request,pk):
    if request.method == 'GET':
        queryset = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)

    
