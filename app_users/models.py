from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, unique=True)
    profile_image = models.ImageField(upload_to='', default='', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

