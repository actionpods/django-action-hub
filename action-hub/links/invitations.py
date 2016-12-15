from django.conf.urls import url
from ..relationships import views


urlpatterns = [
    url(r'^(?P<pod_id>[\d]+)/accept/$', views.respond_to_invitation, {'resp': 'a'}, name='accept_request'),
    url(r'^(?P<pod_id>[\d]+)/decline/$', views.respond_to_invitation, {'resp': 'd'}, name='decline_request'),
]
