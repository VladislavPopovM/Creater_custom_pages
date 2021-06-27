from django.urls import path
from .views import (
    PageListAPIView, PageRetrieveAPIView, ImageRetrieveAPIView,
    AudioRetrieveAPIView, VideoRetrieveAPIView, TextRetrieveAPIView,
)

urlpatterns = [
    path('', PageListAPIView.as_view(), name = 'page'),
    path('<int:pk>/', PageRetrieveAPIView.as_view(), name = 'page_detail'),
    path('image/<int:pk>/', ImageRetrieveAPIView.as_view(), name = 'image_detail'),
    path('text/<int:pk>/', TextRetrieveAPIView.as_view(), name = 'text_detail'),
    path('video/<int:pk>/', VideoRetrieveAPIView.as_view(), name = 'video_detail'),
    path('audio/<int:pk>/', AudioRetrieveAPIView.as_view(), name = 'audio_detail'),
]