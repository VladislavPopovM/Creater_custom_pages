from rest_framework import serializers
from ..models import Page, Image, Audio, Video, Text

class PageSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'title','counter', 'detail_url')
        model = Page

    def get_detail_url(self, obj):
        return f"http://localhost:8000/{obj.id}/"

class PageDetailSerializer(serializers.ModelSerializer):
    texts  = serializers.HyperlinkedIdentityField(view_name='text_detail', many=True)
    videos = serializers.HyperlinkedIdentityField(view_name='video_detail', many=True)
    audios = serializers.HyperlinkedIdentityField(view_name='audio_detail', many=True)
    images = serializers.HyperlinkedIdentityField(view_name='image_detail', many=True)

    class Meta:
        fields = ('__all__')
        model = Page

class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Image

class AudioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Audio

class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Video

class  TextDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Text