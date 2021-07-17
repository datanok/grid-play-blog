from django.urls import path
from .views import (
    DeletePostView,
    HomeView,
    PostDetailView,
    CreatePostView,
    EditPostView,
    AddCommentView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-details"),
    path("create_post/", CreatePostView.as_view(), name="create-posts"),
    path("post/edit_post/<int:pk>", EditPostView.as_view(), name="edit-posts"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="delete-post"),
    path("article/<int:pk>/comment", AddCommentView.as_view(), name="add_comment"),
]
