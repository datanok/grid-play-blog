from django.db import models
from blog.models import Post, UserProfile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm,
)
from django.views.generic import (
    CreateView,
)
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from .forms import EditProfileForm, ProfilePageForm, SignUpForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


class ShowProfileView(DetailView):
    model = UserProfile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        users = UserProfile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        current_user = get_object_or_404(UserProfile, id=self.kwargs["pk"])
        context["current_user"] = current_user

        return context


class EditUserProfileView(generic.UpdateView):
    model = UserProfile
    template_name = "registration/edit_user_profile.html"
    fields = ["bio", "profile_pic", "fb_url", "twitter_url", "instagram_url"]

    success_url = reverse_lazy("home")


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("password_success")


def password_success(request):
    return render(request, "registration/password_changed.html")


class CreateProfilePageView(CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile.html"

    def form_valid(self, form):  # when the user creates the profile, take their user id
        form.instance.user = self.request.user
        return super(CreateProfilePageView, self).form_valid(form)
