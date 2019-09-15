# from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


def profile_pic_directory_with_uuid(instance, filename):
    return f"{instance.profile.raw_username}{uuid4()}"


class Profile(models.Model):
    """
    Profile model for user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    raw_username = models.CharField(max_length=50, blank=True)
    phone = models.CharField(_("Phone"), max_length=11, blank=True)
    bio = models.TextField(_("Short Bio"), max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.raw_username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created,  **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class UserImage(models.Model):
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(
        _("Display Picture"),
        upload_to=profile_pic_directory_with_uuid,
        blank=True)
    uploaded = models.DateTimeField(auto_now=True)
