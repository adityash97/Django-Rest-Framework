from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import generics,mixins,status
from watchlist_app.models import WatchList,StreamPlatform,Review
from .serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import AdminOrReadOnly,ReviewUserOrReadOnly
from django.core.exceptions import ValidationError


class  WatchListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class WatchListDetailsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movies)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movies, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk): #TODO : if else for item not found.
        movies = WatchList.objects.get(pk=pk).delete()
        return Response({'msg':f'movie with ID :  {pk} is deleted'})
    
"""
#API View
class StreamPlatformAPIView(APIView):
    def get(self,request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlatformDetailsAPIView(APIView):
    def get(self,request,pk):
        try:
            queryset = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Not Found'},status= status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(queryset)
        return Response(serializer.data)
    
    def put(self,request,pk):
        queryset = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            queryset = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Not Found'},status= status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({'msg':'Deleted Sucessfully'},status= status.HTTP_204_NO_CONTENT)
"""

# Concrete View Class
class StreamPlatformAPIView(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class StreamPlatformDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

"""
# API View
class ReviewAPIView(APIView):
    def get(self,request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ReviewDetiailsAPIView(APIView):
    def get(self,request,pk):
        try:
            queryset = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'msg':'Does not exist.'},status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            queryset = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'msg':'Does not exist.'},status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(queryset,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            queryset = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'msg':'Does not exist.'},status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response({'msg':'Deleted'},status=status.HTTP_204_NO_CONTENT)
"""

"""
Generic API View to help us to keep our code DRY(do not repeat yourself)
"""

class ReviewAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):  # overriding queryset.
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    # def post(self,request):
    #     return self.create(request)

class ReviewDetiailsAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ReviewCreate(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = ReviewSerializer
    def perform_create(self, serializer): 
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk = pk)
        review_user = self.request.user
        # one person can add only one review.
        review_queryset = Review.objects.filter(watchlist=watchlist,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You already have reveiwed this movie!")
        
        # update avg review and total review
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating+serializer.validated_data['rating'])/2
        
        watchlist.number_rating+=1
        watchlist.save()
        serializer.save(watchlist=watchlist,review_user=review_user)
                
        
