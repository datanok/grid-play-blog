from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm,
)
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import fields, widgets
from blog.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    last_name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    is_superuser = forms.CharField(
        max_length=50, widget=forms.CheckboxInput(attrs={"class": "form-check"})
    )
    is_staff = forms.CharField(
        max_length=50, widget=forms.CheckboxInput(attrs={"class": "form-check"})
    )
    is_active = forms.CharField(
        max_length=50, widget=forms.CheckboxInput(attrs={"class": "form-check"})
    )
    date_joined = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
            "date_joined",
            "is_staff",
            "is_active",
        ]


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )
    new_password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )
    new_password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}),
    )

    class Meta:
        model = User
        fields = [
            "old_password",
            "new_password1",
            "new_password2",
        ]


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("bio", "profile_pic", "fb_url", "twitter_url", "instagram_url")
        widgets = {
            "bio": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter Bio"}
            ),
            "fb_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter facebook url",
                }
            ),
            "twitter_url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter twitter url"}
            ),
            "instagram_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Instagram URL ",
                }
            ),
        }
