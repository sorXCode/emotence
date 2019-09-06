# from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
# from djang


# class CustomUserManager(UserManager):
#     def get_by_natural_key(self, username):
#         return self.get(**{self.model.USERNAME_FIELD + '__iexact': username})


class UserModel(AbstractUser):
    """
    User model for user
    """
    #create a one to one relateion to User model to obey atomicity rule
    # objects = CustomUserManager
    raw_username = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.raw_username

    # def get_absolute_url(self):
    #     return reverse("userbase_detail", kwargs={"pk": self.pk})
