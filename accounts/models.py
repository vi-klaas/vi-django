from django.db import models
from django.contrib.auth.models import AbstractUser

from mixins.uuid_model_mixin import UUIDMixin


# Create your models here.
class Address(UUIDMixin, models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)

    @property
    def full_address(self):
        return f"{self.street}, {self.zip_code}, {self.city}, {self.state}, {self.country}"

    class Meta:
        abstract = True


class ShippingAddress(Address):
    pass


class BillingAddress(Address):
    pass


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    shipping_address = models.ForeignKey('ShippingAddress', related_name="shipping_user", on_delete=models.SET_NULL, null=True, blank=True)
    billing_address = models.ForeignKey('BillingAddress', related_name="billing_user", on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
