from django.urls import path
from .views import (
    CreateProfilePageView,
    ShowProfileView,
    UserRegisterView,
    UserEditView,
    PasswordsChangeView,
    EditUserProfileView,
)
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path(
        "password/",
        PasswordsChangeView.as_view(template_name="registration/change-password.html"),
    ),
    path("password_success", views.password_success, name="password_success"),
    path("<int:pk>/profile", ShowProfileView.as_view(), name="show_profile"),
    path(
        "<int:pk>/edit_user_profile/",
        EditUserProfileView.as_view(),
        name="edit_userprofile",
    ),
    path(
        "create_user_profile/",
        CreateProfilePageView.as_view(),
        name="create_user_profile",
    ),
]
