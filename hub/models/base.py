from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    creator = models.ForeignKey(User, related_name='pod_creator')
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    admins = models.ManyToManyField(User, blank=True)
    private = models.BooleanField(default=False)

    def is_creator(self, user):
        return self.creator == user

    def is_admin(self, user):
        return user in self.admins.all()
