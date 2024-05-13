import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(blank=False, null=True, unique=True)
    image = models.ImageField(blank=True, null=True, default=None)
    about = models.TextField(max_length=500, null=True, blank=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email

    def upload_path(self, filename):
        """
        get the path to upload to
        """
        return os.path.join(str(uuid4()))


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return self.user_id


class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="notes", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
