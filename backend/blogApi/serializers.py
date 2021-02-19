from rest_flex_fields import FlexFieldsModelSerializer
from .models import Post, Category, Comment, MyImage
from django.contrib.auth.models import User
from rest_framework import serializers


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
        expandable_fields = {
            'posts': ('blogApi.PostSerializer', {'many': True})
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'email']


class LikedBySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Post
        fields = ['pk']


class PostUnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        instance.likedBy.remove(user.pk)
        instance.save()
        return instance


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category',)

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


properties = ['title', 'content', 'category', 'likedBy']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'likedBy']

    def update(self, instance, validated_data):
        user = self.context['request'].user
        instance.likedBy.add(user.pk)
        instance.save()
        return instance


class PostSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author',
                  'category', 'created', 'likedBy', 'pk')
        expandable_fields = {
            'category': ('blogApi.CategorySerializer', {'many': True}),
            'comments': ('blogApi.CommentSerializer', {'many': True}),
            'likedBy': ('blogApi.LikedBySerializer', {'many': True}),
            'author': ('blogApi.UserSerializer', {'many': False})
        }

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.is_superuser:
            for k in validated_data:
                if 'title' == k:
                    instance.title = validated_data['title']
                elif 'content' == k:
                    instance.content = validated_data['content']
                elif 'category' == k:
                    instance.category.set(validated_data['category'])
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
    username = serializers.CharField(source='get_username')

    class Meta:
        model = Comment
        fields = ['pk', 'created', 'content', 'liked_by', 'author', 'username']
        read_only_fields = (
            'username',
        )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'post']

    def create(self, validated_data):
        user = self.context['request'].user
        comment = Comment.objects.create(
            content=validated_data['content'], author=user, post=validated_data['post'])
        return comment


class MyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyImage
        fields = ['title', 'image']
