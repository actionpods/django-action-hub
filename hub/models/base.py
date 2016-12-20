from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify


class BaseModel(models.Model):
    creator = models.ForeignKey(User, related_name='pod_creator')
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    admins = models.ManyToManyField(User, blank=True)
    private = models.BooleanField(default=False)

    def is_creator(self, user):
        return self.creator == user

    def is_admin(self, user):
        return user in self.admins.all()



class Focus(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Focus, self).save(*args, **kwargs)
