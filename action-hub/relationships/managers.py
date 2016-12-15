from django.db import models
from django.db.models import Q

class InvitationManager(models.Manager):

    def remove(self, coalition, pod):
        invitations = self.filter(coalition=coalition, pod=pod)
        if not invitations:
            invitations = self.filter(coalition=pod, pod=coalition)
        if invitations:
            invitations.delete()


class BlockingManager(models.Manager):

    def blocked_for_coalition(self, coalition):
        blocked = []
        qs = self.filter(coalition=coalition).select_related(depth=1)
        for blocking in qs:
            blocked.append(blocking.pod)
        return blocked
