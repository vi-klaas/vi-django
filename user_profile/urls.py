from django.urls import path

from . import (
    views,
)  # Assuming your views are in a file called views.py in the same directory

app_name = "user_profile"

urlpatterns = [
    path("", views.UserProfileListView.as_view(), name="userprofile_list"),
    path("new", views.UserProfileCreateView.as_view(), name="userprofile_new"),
    path(
        "<uuid:pk>/", views.UserProfileUpdateView.as_view(), name="userprofile_detail"
    ),
    path(
        "<uuid:pk>/edit/",
        views.UserProfileUpdateView.as_view(),
        name="userprofile_update",
    ),
]
