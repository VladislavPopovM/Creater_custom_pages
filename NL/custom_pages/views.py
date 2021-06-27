from django.shortcuts import render
from rest_framework import generics
from .api.serializers import (
    PageSerializer, PageDetailSerializer, ImageDetailSerializer,
    AudioDetailSerializer, VideoDetailSerializer, TextDetailSerializer,
    )
from .models import Page, Image, Audio, Video, Text

class PageListAPIView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Page.objects.all()
    serializer_class = PageDetailSerializer

    def get(self, request, *args, **kwargs):
        _object = Page.objects.get(id = kwargs['pk'])
        _object.counter = _object.counter + 1
        _object.save()
        return self.retrieve(request, *args, **kwargs)

class ImageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageDetailSerializer

    def get(self, request, *args, **kwargs):
        _object = Image.objects.get(id = kwargs['pk'])
        _object.counter = _object.counter + 1
        _object.save()
        return self.retrieve(request, *args, **kwargs)

class AudioRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioDetailSerializer

    def get(self, request, *args, **kwargs):
        _object = Audio.objects.get(id = kwargs['pk'])
        _object.counter = _object.counter + 1
        _object.save()
        return self.retrieve(request, *args, **kwargs)
    
class VideoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer

    def get(self, request, *args, **kwargs):
        _object = Video.objects.get(id = kwargs['pk'])
        _object.counter = _object.counter + 1
        _object.save()
        return self.retrieve(request, *args, **kwargs)

class TextRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Text.objects.all()
    serializer_class = TextDetailSerializer

    def get(self, request, *args, **kwargs):
        _object = Text.objects.get(id = kwargs['pk'])
        _object.counter = _object.counter + 1
        _object.save()
        return self.retrieve(request, *args, **kwargs)
# Create your views here.
