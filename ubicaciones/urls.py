# -*- encoding: utf-8 -*-
from django.conf.urls import include, patterns, url

from views import ViaList, ViaDetail

via_urls = patterns('',
	url(r'^(?P<cod>[0-9a-zA-Z]+)/', ViaDetail.as_view(), name='via-detail'),
	url(r'^', ViaList.as_view(), name='via-list'),
)

urlpatterns = patterns('ubicaciones.views',
	url(r'^vias/', include(via_urls)),
)