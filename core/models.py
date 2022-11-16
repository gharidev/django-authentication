from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField("Email address", unique=True)
    age = models.IntegerField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []