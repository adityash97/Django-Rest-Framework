from django.urls import path
from .views import movieList,movieDetails,ReviewListAPIView,ReviewDetailsAPIView

urlpatterns =[
    path('movie/',movieList,name='movie-list'),
    path('movie/<int:pk>/',movieDetails,name='movie-details'),
    path('review/',ReviewListAPIView.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetailsAPIView.as_view(),name='review-details'),
    
]