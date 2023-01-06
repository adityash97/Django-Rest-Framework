from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response


class MovieList(APIView):
    def get(self,request):
        return Response({'msg':'success'},status=status.HTTP_200_OK)
    
    def post(self,request):
        return Response({'msg':'success'},status=status.HTTP_200_OK)
    
