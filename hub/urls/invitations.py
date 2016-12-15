from django.conf.urls import url
from hub.views.relationships import RelationShipView


urlpatterns = [
    url(r'^(?P<pod_id>[\d]+)/accept/$', RelationShipView.respond_to_invitation, {'resp': 'a'}, name='accept_request'),
    url(r'^(?P<pod_id>[\d]+)/decline/$', RelationShipView.respond_to_invitation, {'resp': 'd'}, name='decline_request'),
]
