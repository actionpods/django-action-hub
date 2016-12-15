from django.conf.urls import url, include
from ..views import campaign

urlpatterns = [
url(r'^$', campaign.Index.as_view(), name="index"),
url(r'^(?P<pk>[0-9]+)/$', campaign.Detail.as_view(), name="detail"),
url(r'^create/$', campaign.Create.as_view(), name="create"),
url(r'^(?P<pk>[0-9]+)/edit/$', campaign.Update.as_view(), name="edit"),
url(r'^(?P<pk>[0-9]+)/delete/$', campaign.Delete.as_view(), name="delete"),
]
