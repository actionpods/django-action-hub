from rest_framework import viewsets

from django.contrib.auth.models import User
from .models.pod import Pod, Action
from .models.campaign import Campaign
from .serializers import PodSerializer, CampaignSerializer, ActionSerializer

from rest_framework import filters, permissions

class PodViewSet(viewsets.ReadOnlyModelViewSet):
    #This viewset automatically provides `list` and `detail` actions.
    queryset = Pod.objects.all()
    serializer_class = PodSerializer

class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    #This viewset automatically provides `list` and `detail` actions.
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    #search_fields = ('user__username','^user__email','address', 'city')

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
