
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins
from movielist_app.models import Movie,Review
from .serializers import MovieSerializer,ReviewSerializer

class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailsAPIView(generics.GenericAPIView,mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



  
class ReviewListAPIView(APIView):
    def get(self,request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class ReviewDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):        
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

            
