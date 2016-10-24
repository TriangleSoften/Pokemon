from django.conf.urls import url
from django.contrib import admin

from .views import (
	allcatalog,
	)

urlpatterns = [
	url(r'^$', allcatalog),
    #url(r'^create/$', post_create),
    #url(r'^detail/$', post_detail),
    #url(r'^update/$', post_update),
    #url(r'^delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]




