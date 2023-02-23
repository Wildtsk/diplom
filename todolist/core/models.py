from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'
