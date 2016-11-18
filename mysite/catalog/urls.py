from django.conf.urls import url
from django.contrib import admin

from .views import (
	allcatalog,
	)

urlpatterns = [
	url(r'^$', allcatalog),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]




