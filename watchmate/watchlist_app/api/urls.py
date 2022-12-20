from django.urls import path
from .views import MovieAPIView,MovieDetailsAPIView

urlpatterns = [
    path('list/',MovieAPIView.as_view(), name='movie_list'),
    path('<int:pk>/',MovieDetailsAPIView.as_view(), name='movie_details'),
]