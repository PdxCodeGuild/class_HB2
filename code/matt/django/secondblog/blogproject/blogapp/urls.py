from django.urls import path
from .views import ProfileView, ArticleView, CreatePostView, UpdatePostView, DeletePostView

#Creating ProfileView, ArticleView, CreatePostView, etc... for the ease of a view

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete'),
]
