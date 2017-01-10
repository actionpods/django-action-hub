from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_delete, post_save
from django.contrib.auth.models import User

from hub.models.pod import Pod
from hub.models.campaign import Campaign
from django.db.models import Q

from accounts.models import Profile

class HubProfile(Profile):
    pod_endorsements = models.ManyToManyField(Pod, related_name='pod_endorsements')
    campaign_endorsements = models.ManyToManyField(Campaign, related_name='campaign_endorsements')

class InvitationManager(models.Manager):

    def remove(self, campaign, pod):
        invitations = self.filter(campaign=campaign, pod=pod)
        if not invitations:
            invitations = self.filter(campaign=pod, pod=campaign)
        if invitations:
            invitations.delete()


class BlockingManager(models.Manager):

    def blocked_for_campaign(self, campaign):
        blocked = []
        qs = self.filter(campaign=campaign).select_related(depth=1)
        for blocking in qs:
            blocked.append(blocking.pod)
        return blocked

class Blocking(models.Model):
    """
    A campaign can block a pod from requesting to join
    """

    campaign = models.ForeignKey(Campaign, verbose_name=_("campaign that is blocking"), related_name="blocking")
    pod = models.ForeignKey(Pod, verbose_name=_("pod that is blocked"), related_name="blocked_by")
    added = models.DateTimeField(_("added"), auto_now=True)

    objects = BlockingManager()


class Invitation(models.Model):
    """
    A pod will send a request to join the Campaign
    """

    campaign = models.ForeignKey(Campaign, verbose_name=_("request to join campaign"), related_name="invitations_to")
    pod = models.ForeignKey(Pod, verbose_name=_("from pod"), related_name="invitations_from")
    message = models.TextField(_("message"))
    sent = models.DateTimeField(_("sent"), auto_now=True)

    objects = InvitationManager()

    def accept(self):
        if not self.pod in self.campaign.pods.all():
            self.campaign.pods.add(self.pod)
        self.delete()

    def decline(self):
        self.delete()
