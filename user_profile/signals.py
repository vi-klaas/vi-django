"""
Signals for user_profile app.
"""
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create User Profile

    Create a user profile when a new user is saved.

    :param sender: The sender of the signal.
    :param instance: The instance of the user being saved.
    :param created: A boolean indicating if the user is being created or updated.
    :param kwargs: Additional keyword arguments passed to the receiver.
    :return: None
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save User Profile

    This method is a signal handler that listens for the `post_save` event of the `User` model and saves the associated `UserProfile` instance.

    :param sender: The sender of the signal.
    :param instance: The instance of the `User` model that triggered the signal.
    :param kwargs: Additional keyword arguments.

    :return: None
    """
    instance.profile.save()
