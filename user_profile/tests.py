import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from rest_framework import status

from .models import UserProfile

User = get_user_model()

@pytest.mark.django_db
def test_user_profile_view():
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    UserProfile.objects.create(user=user, position='AD')
    res = client.get(reverse("user_profile_detail", kwargs={'pk': 1}))
    assert res.status_code == status.HTTP_200_OK
    assert "testuser" in str(res.content)

@pytest.mark.django_db
def test_user_profile_view_edit():
    client = Client()
    user = User.objects.create_user(username='testuser', password='12345')
    UserProfile.objects.create(user=user, position='AD')
    client.login(username='testuser', password='12345')
    res = client.get(reverse("user_profile_update", kwargs={'pk': 1}))
    assert res.status_code == status.HTTP_200_OK
    assert "testuser" in str(res.content)
