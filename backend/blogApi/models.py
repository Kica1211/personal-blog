from django.db import models
from django.contrib.auth.models import User


class MyImage(models.Model):
    title = models.CharField(max_length=100, default="me")
    image = models.ImageField(upload_to='images/')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likedBy = models.ManyToManyField(User, related_name='posts', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    likedBy = models.ManyToManyField(User, blank=True)

    def get_comment_likes(self):
        users = []
        for user in self.likedBy.all():
            users.append(user.username)
        return users
