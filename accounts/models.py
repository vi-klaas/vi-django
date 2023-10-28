from django.contrib.auth.models import AbstractUser
from django.db import models

from mixins.uuid_model_mixin import UUIDMixin


# Create your models here.
class Profile(UUIDMixin, models.Model):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        abstract = True


class Address(UUIDMixin, models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False)

    @property
    def full_address(self):
        return f"{self.street}, {self.zip_code}, {self.city}, {self.state}, {self.country}"

    class Meta:
        abstract = True


class User(AbstractUser):

    @property
    def full_name(self):
        """
        Return the full name of the user.

        :return: The full name of the user as a string.
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username


class ShippingAddress(Address):
    user = models.ForeignKey(User, related_name="shipping_address", on_delete=models.SET_NULL, null=True, blank=True)


class BillingAddress(Address):
    user = models.ForeignKey(User, related_name="billing_address", on_delete=models.SET_NULL, null=True, blank=True)
