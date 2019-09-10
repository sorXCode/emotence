# from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


def profile_pic_directory_with_uuid(instance, filename):
    return "{instance.raw_user}{uuid4()}"


# class CustomUserManager(UserManager):
#     def get_by_natural_key(self, username):
#         return self.get(**{self.model.USERNAME_FIELD + '__iexact': username})


class Profile(models.Model):
    """
    User model for user
    """
    # create a one to one relateion to User model to obey atomicity rule
    # objects = CustomUserManager
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    raw_username = models.CharField(max_length=50, blank=False)
    bio = models.TextField(_("Short Bio"), max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(
        _("Display Picture"), upload_to=profile_pic_directory_with_uuid)

    def __str__(self):
        return self.raw_username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created,  **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
