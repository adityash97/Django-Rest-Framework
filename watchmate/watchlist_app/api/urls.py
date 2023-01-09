from django.urls import path
from .views import (WatchListAPIView,WatchListDetailsAPIView,
                    StreamPlatformAPIView,StreamPlatformDetailsAPIView,
                    ReviewAPIView,ReviewDetiailsAPIView,ReviewCreate)

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
    path('<int:pk>/review/',ReviewAPIView.as_view(),name="stream-review-all"),
    # review details for a review
    path('review/<int:pk>/',ReviewDetiailsAPIView.as_view(), name='stream-review-details'),
    # create review for perticular movie
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name="stream-review-create"),
    
    
]