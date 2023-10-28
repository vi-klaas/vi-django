# forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, Department, CareerPosition

User = get_user_model()


class UserProfileForm(UserCreationForm):
    email = forms.EmailField(required=True)
    departments = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(), required=False
    )
    position = forms.ChoiceField(choices=CareerPosition.choices, required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "departments",
            "position",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        user_profile = UserProfile(user=user, position=self.cleaned_data["position"])
        user_profile.departments.set(self.cleaned_data["departments"])
        user_profile.save()
        return user, user_profile
