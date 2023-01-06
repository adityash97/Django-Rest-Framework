from django.urls import path
from .views import movieList,movieDetails

urlpatterns =[
    path('movie/',movieList,name='movie-list'),
    path('movie/<int:pk>/',movieDetails,name='movie-details')
]