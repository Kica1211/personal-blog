from .serializers import PostSerializer, MyImageSerializer
from .models import Post, MyImage
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


class PostViewSet(FlexFieldsMixin, generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permit_list_expands = ['category', 'comments']


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetail(FlexFieldsMixin, generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        post = Post.objects.filter(id=self.kwargs['pk'])
        return post


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class ImagesList(generics.ListAPIView):
    queryset = MyImage.objects.all()
    serializer_class = MyImageSerializer
