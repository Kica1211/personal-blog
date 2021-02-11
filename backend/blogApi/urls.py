from django.urls import path
from blogApi.views import PostViewSet, PostCreate, PostDetail, PostUpdate, PostDelete, ImagesList
urlpatterns = [
    path('post-create/', PostCreate.as_view(), name="post-create"),
    path('posts-list/', PostViewSet.as_view(), name='posts-list'),
    path('post-detail/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post-create/', PostCreate.as_view(), name="post-create"),
    path('post-update/<int:pk>/', PostUpdate.as_view(), name="post-update"),
    path('post-delete/<int:pk>/', PostDelete.as_view(), name="post-delete"),
    path('images/', ImagesList.as_view(), name="images-list")
]
