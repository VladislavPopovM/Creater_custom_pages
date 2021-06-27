from django.db import models

class Page(models.Model):
    title =  models.CharField(max_length = 128)
    counter = models.PositiveIntegerField(default=0)
    texts = models.ManyToManyField("Text", blank = True)
    videos = models.ManyToManyField("Video", blank = True)
    audios = models.ManyToManyField("Audio", blank = True)
    images = models.ManyToManyField("Image", blank = True)

    def __str__(self):
        return self.title

class Text(models.Model):
    title =  models.CharField(max_length = 128)
    counter = models.PositiveIntegerField(default=0)
    content = models.TextField()
    priority = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class Video(models.Model):
    title =  models.CharField(max_length = 128)
    counter = models.PositiveIntegerField(default=0)
    content = models.FileField(upload_to='video/')
    priority = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class Audio(models.Model):
    title =  models.CharField(max_length = 128)
    counter = models.PositiveIntegerField(default=0)
    content = models.FileField(upload_to='audio/')
    priority = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class Image(models.Model):
    title =  models.CharField(max_length = 128)
    counter = models.PositiveIntegerField(default=0)
    content = models.FileField(upload_to='image/')
    priority = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title