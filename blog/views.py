from django.db import models
from django.db.models.fields import files
from django.urls.base import reverse, reverse_lazy
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment
from .forms import PostForm, AddCommmentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date"]  # orders posts by date
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "create_post.html"


class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "edit_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommmentForm
    template_name = "add_comment.html"

    def get_success_url(self):
        return reverse_lazy("post-details", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super(AddCommentView, self).form_valid(form)
