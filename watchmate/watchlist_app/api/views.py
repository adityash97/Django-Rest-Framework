from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import Movie
from .serializers import MovieSerializer


class  MovieAPIView(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class MovieDetailsAPIView(APIView):
    
    def get(self,request,pk):
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk): #TODO : if else for item not found.
        movies = Movie.objects.get(pk=pk).delete()
        return Response({'msg':f'movie with ID :  {pk} is deleted'})