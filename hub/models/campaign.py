from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify

from .base import BaseModel
from .coalition import Coalition

class Campaign(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    coalitions = models.ManyToManyField(Coalition, related_name='campaign_coalitions', blank=True)
    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Campaign, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("actionpods:campaign:detail", kwargs={'pk': self.id})
