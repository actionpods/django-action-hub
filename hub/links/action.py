from django.conf.urls import url, include

from ..views import action

urlpatterns = [
    url(r'^action/(?P<slug>[-\w]+)/delete/$', action.Delete.as_view(), name="delete"),
    url(r'^action/(?P<slug>[-\w]+)/$', action.Detail.as_view(), name="detail"),
    url(r'^action/(?P<slug>[-\w]+)/edit/$', action.Update.as_view(), name="edit"),
]
