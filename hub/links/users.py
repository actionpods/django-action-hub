from django.conf.urls import url, include
from ..views import user

urlpatterns = [
    url(r'^$', user.index, name="index"),
    url(r'^(?P<user>[0-9])/$', user.detail, name="detail"),
]
