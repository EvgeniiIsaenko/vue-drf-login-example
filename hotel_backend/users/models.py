from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

from uuid import uuid4

# User model
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4) # id is the primary key
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True) # middle name is optional as not everyone has one
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False) # whether the user is a manager who has edit privileges
    # TODO: add: phone_num, email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    objects = CustomUserManager()

    def __str__(self):
        return str(self.id)