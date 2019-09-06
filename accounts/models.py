from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=11)
