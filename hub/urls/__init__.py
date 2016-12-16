from django.conf.urls import url, include

from hub.views import profile as views_profile
from hub.views import action as views_action

from hub.urls import action, campaign, pod, users


urlpatterns = [
            url(r'^$', views_profile.index, name="dashboard"),
            url(r'^action/', include(action, namespace='action')),
            url(r'^campaign/', include(campaign, namespace='campaign')),
            url(r'^pod/', include(pod, namespace='pod')),
            url(r'^users/', include(users, namespace='user')),

            url(r'^pod/(?P<pk>[0-9]+)/action/create/$', views_action.Create.as_view(), name="action_create"),


            ]
