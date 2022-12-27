from django.urls import path
from .views import WatchListAPIView,WatchListDetailsAPIView,StreamPlatformAPIView,StreamPlatformDetailsAPIView

urlpatterns = [
    path('list/' ,WatchListAPIView.as_view(), name='watchlist'),
    path('<int:pk>/',WatchListDetailsAPIView.as_view(), name='watchlist_details'),
    path('stream/',StreamPlatformAPIView.as_view(),name="stream"),
    path('stream/<int:pk>',StreamPlatformDetailsAPIView.as_view(),name="stream_details"),
]