from django.urls import path

from cms_app.views import PostCreateAPIView, UserCreateAPIView, UserPostsAPIView, UserRetrieveAPIView

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/me/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('posts/', PostCreateAPIView.as_view(), name='post-create'),
    path('my-posts/', UserPostsAPIView.as_view(), name='user-posts'),
]
