"""
user_profile app configuration
"""
from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """

    The `UserProfileConfig` class is a Django app configuration class for the `user_profile` app.

    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "user_profile"

    def ready(self):
        import user_profile.signals  # noqa
