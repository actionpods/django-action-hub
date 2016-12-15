
from django.conf.urls import url, include
from hub.views import coalition
from hub.views.relationships import RelationShipView

from . import invitations



urlpatterns = [
    url(r'^$', coalition.Index.as_view(), name="index"),
    url(r'^create/$', coalition.Create.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/$', coalition.Detail.as_view(), name="detail"),
    url(r'^(?P<pk>[0-9]+)/edit/$', coalition.Update.as_view(), name="edit"),
    url(r'^(?P<pk>[0-9]+)/delete/$', coalition.Delete.as_view(), name="delete"),
    ##Invitations
    url(r'^(?P<pk>[0-9]+)/admin/$', RelationShipView.list_received_invitations, name="admin"),
    url(r'^(?P<pk>[0-9]+)/admin/invitation/', include(invitations, namespace='invitations')),
    ##Blogs
    #Put in check for app existence!
    url(r'^(?P<pk>[0-9]+)/blog/$', coalition.blog_index, name="blog"),
]
