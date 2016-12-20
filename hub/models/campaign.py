from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify

from .base import BaseModel, Focus
from .pod import Pod

class Campaign(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    focus = models.ForeignKey(Focus, blank=True)
    pods = models.ManyToManyField(Pod, related_name='campaign_pods', blank=True)
    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Campaign, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("actionpods:campaign:detail", kwargs={'pk': self.id})

try:
    from blog.models import *
    class CampaignBlog(Blog):
        campaign = models.ForeignKey(Campaign)
except ImportError:
    pass
