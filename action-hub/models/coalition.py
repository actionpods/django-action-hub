from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from sorl.thumbnail import ImageField

from django.template.defaultfilters import slugify


from .pod import Pod
from .base import BaseModel

class Coalition(BaseModel):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    pods = models.ManyToManyField(Pod, related_name='coalition_pods', blank=True)
    banner = ImageField(upload_to='coalitions', blank=True)
    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse("actionpods:coalition:detail", kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Coalition, self).save(*args, **kwargs)

try:
    from blog.models import *
    class CoalitionBlog(Blog):
        coalition = models.ForeignKey(Coalition)
except ImportError:
    pass
