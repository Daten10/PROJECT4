from django.db import models


class Slogan(models.Model):

    text = models.CharField(max_length=300)


class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField(verbose_name='enter the video url')


class TopGadgets(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(verbose_name='decription')
    price = models.PositiveIntegerField(default=1000)
    image = models.ImageField()


