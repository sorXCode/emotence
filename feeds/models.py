from django.db import models
from django.utils.translation import ugettext_lazy as _

class Feed(models.Model):

    emtex = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)
    likes = models.IntegerField(_("likes"))
    favorite = models.IntegerField(_("favorite"))
    

    def __str__(self):
        return self.emtex

    # def get_absolute_url(self):
    #     return reverse("feed_detail", kwargs={"pk": self.pk})
