from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from .models.pod import Pod, Action
from .models.campaign import Campaign

class PodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pod
        fields = ('title', 'leader', 'members', 'coalition_pods', 'action_set')

class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Action
        fields = ('title',)

class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ('title', 'pods')
