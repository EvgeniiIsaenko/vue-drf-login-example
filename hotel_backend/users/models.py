from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    textArea = models.TextField(default='')

    def __str__(self) -> str:
        return self.username 