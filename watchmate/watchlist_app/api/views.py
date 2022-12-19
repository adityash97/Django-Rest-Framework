from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from .serializers import MovieSerializer

@api_view(['GET','POST'])
def movie_list(request):
    if(request.method == 'GET'):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    elif request.method == 'POST': 
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):
    movies = Movie.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    elif request.method == 'PUT':
       serializer = MovieSerializer(movies, data = request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors)
    elif request.method == 'DELETE': #TODO : if else for item not found.
        movies = Movie.objects.get(pk=pk).delete()
        return Response({'msg':f'movie with ID :  {pk} is deleted'})