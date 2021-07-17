from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "author",
            "body",
            "snippet",
            "header_img",
            "post_thumbnail",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Blog Title"}
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter AUthor",
                    "id": "author",
                    "value": "",
                    "type": "hidden",
                }
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Blog Content"}
            ),
            "snippet": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Snippet To Display ",
                }
            ),
        }


class AddCommmentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Name"}
            ),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Comment"}
            ),
        }