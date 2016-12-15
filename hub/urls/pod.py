from django.conf.urls import url, include
from hub.views import pod

urlpatterns = [
    url(r'^$', pod.Index.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', pod.Detail.as_view(), name="detail"),
    url(r'^create/$', pod.Create.as_view(), name="create"),
    url(r'^(?P<pk>[0-9]+)/delete/$', pod.Delete.as_view(), name="delete"),
    url(r'^(?P<pk>[0-9]+)/edit/$', pod.Update.as_view(), name="edit"),
    #url(r'^(?P<pk>[0-9]+)/admin/$', views.list_sent_invitations, name="admin"),

]
