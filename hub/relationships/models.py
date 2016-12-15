from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_delete, post_save
from django.contrib.auth.models import User

from ..models.pod import Pod
from ..models.coalition import Coalition
from .managers import InvitationManager, BlockingManager

class Blocking(models.Model):
    """
    A coalition can block a pod from requesting to join
    """

    coalition = models.ForeignKey(Coalition, verbose_name=_("coalition that is blocking"), related_name="blocking")
    pod = models.ForeignKey(Pod, verbose_name=_("pod that is blocked"), related_name="blocked_by")
    added = models.DateTimeField(_("added"), auto_now=True)

    objects = BlockingManager()


class Invitation(models.Model):
    """
    A pod will send a request to join the Coalition
    """

    coalition = models.ForeignKey(Coalition, verbose_name=_("request to join coalition"), related_name="invitations_to")
    pod = models.ForeignKey(Pod, verbose_name=_("from pod"), related_name="invitations_from")
    message = models.TextField(_("message"))
    sent = models.DateTimeField(_("sent"), auto_now=True)

    objects = InvitationManager()

    def accept(self):
        if not self.pod in self.coalition.pods.all():
            self.coalition.pods.add(self.pod)
        self.delete()

    def decline(self):
        self.delete()
