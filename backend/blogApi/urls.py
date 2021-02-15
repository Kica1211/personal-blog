from django.urls import path
from blogApi.views import PostViewSet, PostCreate, PostDetail, PostUpdate, PostDelete, ImagesList, UserDetail, PostLike, PostUnlike
urlpatterns = [
    path('post-create/', PostCreate.as_view(), name="post-create"),
    path('posts-list/', PostViewSet.as_view(), name='posts-list'),
    path('post-detail/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post-create/', PostCreate.as_view(), name="post-create"),
    path('post-update/<int:pk>/', PostUpdate.as_view(), name="post-update"),
    path('post-unlike/<int:pk>/', PostUnlike.as_view(), name="post-unlike"),
    path('post-like/<int:pk>/', PostLike.as_view(), name="post-like"),
    path('post-delete/<int:pk>/', PostDelete.as_view(), name="post-delete"),
    path('images/', ImagesList.as_view(), name="images-list"),
    path('user-detail/<str:username>/', UserDetail.as_view(), name="user-detail")
]
