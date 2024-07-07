from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager
import uuid


class User(AbstractUser):
    userId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    objects = UserManager()

    # Set username to None to effectively ignore it
    username = None

    # Set the email as the unique identifier
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email

