from django.db import models
from django.contrib.auth import get_user_model


class TimestampedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
