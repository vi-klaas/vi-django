from django.urls import path

from .views import UserDetailView, UserUpdateView

urlpatterns = [
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/edit/', UserUpdateView.as_view(), name='user_update'),
    # Add other accounts-related URLs if needed
]
