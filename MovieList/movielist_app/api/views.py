
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from movielist_app.models import Movie,Review
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
    try:
        queryset = Movie.objects.get(pk=pk)
    except:
        return Response({'msg':'DoesNotExist'},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = MovieSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = MovieSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        try:
            queryset.delete()
            return Response({'msg':'Deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        except queryset.DoesNotExist:
             return Response({'msg':'DoesNotExist'},status=status.HTTP_204_NO_CONTENT)
    
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

class ReviewDetailsAPIView(APIView):
    
    def get(self,request,pk):
        try:
            queryset = Review.objects.get(pk=pk)
        except:
            return Response({'msg':'DoesNotExist'},status=status.HTTP_204_NO_CONTENT)
        serilaizer = ReviewSerializer(queryset)
        return Response(serilaizer.data,status=status.HTTP_200_OK)
        
    
    def put(self,request,pk):
        try:
            queryset = Review.objects.get(pk=pk)
        except:
            return Response({'msg':'DoesNotExist'},status=status.HTTP_204_NO_CONTENT)
        serilaizer = ReviewSerializer(queryset,data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data,status=status.HTTP_200_OK)
        else:
            return Response(serilaizer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        
    def delete(self,request,pk):
        try:
            queryset = Review.objects.get(pk=pk)
        except:
            return Response({'msg':'DoesNotExist'},status=status.HTTP_204_NO_CONTENT)
        
        try:
            queryset.delete()
            return Response({'msg':'Deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        except queryset.DoesNotExist:
             return Response({'msg':'DoesNotExist'},status=status.HTTP_204_NO_CONTENT)
        
        

            
