from django.conf.urls import url, include

from .views import profile, action

urlpatterns = [
            url(r'^$', profile.index, name="dashboard"),
            url(r'^action/', include('actionpods.links.action', namespace='action')),
            url(r'^campaign/', include('actionpods.links.campaign', namespace='campaign')),
            url(r'^coalition/', include('actionpods.links.coalition', namespace='coalition')),
            url(r'^pod/', include('actionpods.links.pod', namespace='pod')),
            url(r'^users/', include('actionpods.links.users', namespace='user')),

            url(r'^pod/(?P<pk>[0-9]+)/action/create/$', action.Create.as_view(), name="action_create"),


            ]
