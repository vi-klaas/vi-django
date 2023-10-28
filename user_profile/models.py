from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Profile
from mixins.timestamped_model_mixin import TimestampedModelMixin
from mixins.uuid_model_mixin import UUIDMixin


class Department(UUIDMixin, TimestampedModelMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    short_name = models.CharField(max_length=8, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


class CareerPosition(models.TextChoices):
    ADMIN = 'AD', _('Admin')
    AA = 'AA', _('Assistant doctor')
    OAIV = 'OI', _('Oberarzt iV')
    OA = 'OA', _('Oberarzt')
    LA = 'LA', _('Leitender Arzt')
    CA = 'CA', _('Chefarzt')


class UserProfile(Profile):
    user = models.OneToOneField(get_user_model(), related_name="profile", on_delete=models.CASCADE)
    departments = models.ManyToManyField(Department, related_name="members", blank=True)
    position = models.CharField(max_length=255, null=True, blank=True, choices=CareerPosition.choices)

    def __str__(self):
        return self.user.full_name
