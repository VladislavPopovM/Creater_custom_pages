from django.contrib import admin
from .models import Page, Text, Video, Audio, Image


@admin.register(Page, Text, Video, Audio, Image)
class PageAdmin(admin.ModelAdmin):
    search_fields = ('title',)

