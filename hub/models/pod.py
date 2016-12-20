from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify

from tinymce.models import HTMLField

from .base import BaseModel, Focus
#A collection of people with a common set of goals
class Pod(BaseModel):
    team_size = models.IntegerField(default = 1)
    members = models.ManyToManyField(User, blank=True, related_name='pod_members')
    description = HTMLField(null=True, blank=True)
    focus = models.ForeignKey(Focus, blank=True)
    ally_pods = models.ManyToManyField('self', blank=True)

    def _get_title(self):
        return '%s\'s %s' % (self.creator.username, self.focus.title)
    title = property(_get_title)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse("actionpods:pod:detail", kwargs={'pk': self.id})

#A clearly defined action (e.g. protests, voter calls, door knocking)
class Action(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    pod = models.ForeignKey(Pod, blank=True)
    description = HTMLField(null=True, blank=True)
    #If applicable, set event time
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Action, self).save(*args, **kwargs)

    def get_absolute_url(self):
        #return reverse("actionpods:action", kwargs={'pk': self.pod.id, 'slug': self.slug})
        return reverse("actionpods:action:detail", kwargs={'slug': self.slug})
