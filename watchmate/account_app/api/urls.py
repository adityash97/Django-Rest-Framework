from django.urls import path
from rest_framework.urls import path
from .views import login

urlpatterns = [
    path('login/',login,name="user-login")
]