from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.urls import reverse

from django.template.defaultfilters import slugify

#CKEditor
from ckeditor.fields import RichTextField

from .base import BaseModel

class PodCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_pod_category', None, { 'slug': self.slug })

#A collection of people with a common set of goals
class Pod(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    team_size = models.IntegerField(default = 1)
    members = models.ManyToManyField(User, blank=True, related_name='pod_members')
    leader = models.ForeignKey(User)
    description = RichTextField(null=True, blank=True)
    categories = models.ManyToManyField(PodCategory, blank=True)

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse("actionpods:pod:detail", kwargs={'pk': self.id})

#A clearly defined action (e.g. protests, robocalls, door knocking)
class Action(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    pod = models.ForeignKey(Pod, blank=True)
    description = RichTextField(null=True, blank=True)
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

#Defined roles for each action
class Role(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    member = models.ForeignKey(User, blank=True, related_name='role_member')
    action = models.ForeignKey(Action)
    def __str__(self):
        return '%s' % self.title
