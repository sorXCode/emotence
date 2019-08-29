# from django.db import models
from django.contrib.auth.models import User


class UserModel(User):
    """
    User model for accounts
    """
    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse("userbase_detail", kwargs={"pk": self.pk})



