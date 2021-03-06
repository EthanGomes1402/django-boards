from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_on').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.CharField(max_length=1000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.char(30)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message,safe_mode='escape'))


class Contact(models.Model):
    name = models.CharField(max_length=50)
    query = models.CharField(max_length=1000)
    email = models.CharField(max_length=100, default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query



