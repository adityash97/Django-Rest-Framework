
from django.shortcuts import render
from rest_framework import generics

from rest_framework import authentication
from rest_framework import permissions

from .models import Product,Base_User
from .serilaizers import ProductDeleteSerializer,ProductSerializer,Base_UserSerializer


class Home(generics.CreateAPIView):
    queryset = Base_User.objects.all()
    serializer_class = Base_UserSerializer

home = Home.as_view()

class Create(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

create = Create.as_view()  

class Update(generics.RetrieveUpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductDeleteSerializer
    lookup_field = 'pk'


update = Update.as_view()

class Delete(generics.RetrieveDestroyAPIView):
    authentication_classes = [
            authentication.SessionAuthentication, authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

delete = Delete.as_view()
