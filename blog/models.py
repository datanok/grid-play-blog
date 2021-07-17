from io import SEEK_CUR
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # this deletes all the blogposts by the user if the user is delted
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=255)
    header_img = models.ImageField(null=True, blank=True, upload_to="images/")
    post_thumbnail = models.ImageField(
        null=True, blank=True, upload_to="images/thumbnails"
    )

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("post-details", kwargs={"pk": self.pk})


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )  # connect with post model
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # now we can see post title and name on admin area
        return "%s - %s" % (self.post.title, self.name)
