from django.urls import path
from .views import WatchListAPIView,WatchListDetailsAPIView,StreamPlatformAPIView,StreamPlatformDetailsAPIView,ReviewAPIView,ReviewDetiailsAPIView

urlpatterns = [
    # Movie all
    path('list/' ,WatchListAPIView.as_view(), name='watchlist'),
    # Movie details for a movie
    path('<int:pk>/',WatchListDetailsAPIView.as_view(), name='watchlist_details'),
    #stream all
    path('stream/',StreamPlatformAPIView.as_view(),name="stream"),
    #stream details for a stream
    path('stream/<int:pk>',StreamPlatformDetailsAPIView.as_view(),name="stream_details"),
    
    # All reviews
    path('review/',ReviewAPIView.as_view(),name="review"),
    # review details for a review
    path('review/<int:pk>/',ReviewDetiailsAPIView.as_view(), name='review_details'),
    
    
]