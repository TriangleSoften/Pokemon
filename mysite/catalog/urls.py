from django.conf.urls import url
from django.contrib import admin

from .views import (
	allcatalog,
	)

urlpatterns = [
	url(r'^$', allcatalog),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
    url(r'^addproduct/$', views.index, name='Index'),
	url(r'^showdata/$', views.showdata),
	url(r'^select/$', views.select),
	url(r'^update/$', views.update),
	url(r'^doUpdate/$', views.doUpdate),
	url(r'^delete/$', views.delete),
]




