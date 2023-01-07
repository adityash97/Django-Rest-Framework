from django.urls import path
from .views import MovieListAPIView,MovieDetailsAPIView,ReviewListAPIView,ReviewDetailsAPIView

urlpatterns =[
    path('movie/',MovieListAPIView.as_view(),name='movie-list'),
    path('movie/<int:pk>/',MovieDetailsAPIView.as_view(),name='movie-details'),
    path('review/',ReviewListAPIView.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetailsAPIView.as_view(),name='review-details'),
    
]