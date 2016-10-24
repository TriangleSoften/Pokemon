from django.conf.urls import url
from django.contrib import admin

from .views import (
	allcatalog,
	skincare,
	base_makeup,
	point_makeup,
	accessories,
	fragrance,
	)

urlpatterns = [
	url(r'^$', allcatalog),
    url(r'^skincare/$', skincare),
    url(r'^base_makeup/$', base_makeup),
    url(r'^point_makeup/$', point_makeup),
    url(r'^accessories/$', accessories),
    url(r'^fragrance/$', fragrance),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]




