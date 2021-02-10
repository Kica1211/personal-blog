from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='posts')
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likedBy = models.ManyToManyField(User, related_name='posts', blank=True)

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    likedBy = models.ManyToManyField(User, blank=True)
