from rest_flex_fields import FlexFieldsModelSerializer
from .models import Post, Category, Comment, MyImage
from django.contrib.auth.models import User
from rest_framework import serializers


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
            'posts': ('blogApi.PostSerializer', {'many': True})
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class LikedBySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'likedBy')
        expandable_fields = {
            'category': ('blogApi.CategorySerializer', {'many': True}),
            'comments': ('blogApi.CommentSerializer', {'many': True}),
            'likedBy': ('blogApi.LikedBySerializer', {'many': True}),
        }

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_superuser:
            post = Post.objects.create(
                author=user, title=validated_data['title'], content=validated_data['content'])
            post.category.set(validated_data['category'])
            return post
        else:
            raise serializers.ValidationError(
                {"authorize": "You are not superuser!"})

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.is_superuser:
            instance.category.set(validated_data['category'])
            instance.title = validated_data['title']
            instance.content = validated_data['content']
            instance.save()
            return instance
        else:
            raise serializers.ValidationError(
                {"authorize": "You are not superuser!"})

    def delete(self, instance):
        user = self.context['request'].user
        if user.is_superuser:
            instance.delete()
        else:
            raise serializers.ValidationError(
                {"authorize": "You are not superuser!"})


class CommentSerializer(FlexFieldsModelSerializer):
    liked_by = serializers.ListField(source='get_comment_likes')

    class Meta:
        model = Comment
        fields = ['content', 'liked_by']
        read_only_fields = (
            'liked_by',
        )


class MyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyImage
        fields = ['title', 'image']
