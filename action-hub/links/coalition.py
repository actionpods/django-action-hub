
from django.conf.urls import url, include
from ..views import coalition
from ..relationships import views

urlpatterns = [
    url(r'^$', coalition.Index.as_view(), name="index"),
    url(r'^create/$', coalition.Create.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/$', coalition.Detail.as_view(), name="detail"),
    url(r'^(?P<pk>[0-9]+)/edit/$', coalition.Update.as_view(), name="edit"),
    url(r'^(?P<pk>[0-9]+)/delete/$', coalition.Delete.as_view(), name="delete"),
    ##Invitations
    url(r'^(?P<pk>[0-9]+)/admin/$', views.list_received_invitations, name="admin"),
    url(r'^(?P<pk>[0-9]+)/admin/invitation/', include('actionpods.links.invitations', namespace='invitations')),
]
