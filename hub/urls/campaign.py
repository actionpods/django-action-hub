from django.conf.urls import url, include
from hub.views import campaign
from hub.views.relationships import RelationShipView

from . import invitations

urlpatterns = [
url(r'^$', campaign.Index.as_view(), name="index"),
url(r'^(?P<pk>[0-9]+)/$', campaign.Detail.as_view(), name="detail"),
url(r'^create/$', campaign.Create.as_view(), name="create"),
url(r'^(?P<pk>[0-9]+)/edit/$', campaign.Update.as_view(), name="edit"),
url(r'^(?P<pk>[0-9]+)/delete/$', campaign.Delete.as_view(), name="delete"),
##Invitations
url(r'^(?P<pk>[0-9]+)/admin/$', RelationShipView.list_received_invitations, name="admin"),
url(r'^(?P<pk>[0-9]+)/admin/invitation/', include(invitations, namespace='invitations')),
##Blogs
#Put in check for app existence!
url(r'^(?P<pk>[0-9]+)/blog/$', campaign.blog_index, name="blog"),
]
